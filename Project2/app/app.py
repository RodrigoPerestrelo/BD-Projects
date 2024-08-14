#!/usr/bin/python3
# Copyright (c) BDist Development Team
# Distributed under the terms of the Modified BSD License.
import os
from logging.config import dictConfig
from datetime import datetime

from flask import Flask, jsonify, request
from psycopg.rows import namedtuple_row
from psycopg_pool import ConnectionPool
import psycopg

# Use the DATABASE_URL environment variable if it exists, otherwise use the default.
# Use the format postgres://username:password@hostname/database_name to connect to the database.
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://saude:saude@postgres/saude")

pool = ConnectionPool(
    conninfo=DATABASE_URL,
    kwargs={
        "autocommit": True,  # If True don’t start transactions automatically.
        "row_factory": namedtuple_row,
    },
    min_size=4,
    max_size=10,
    open=True,
    # check=ConnectionPool.check_connection,
    name="postgres_pool",
    timeout=5,
)

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s:%(lineno)s - %(funcName)20s(): %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

app = Flask(__name__)
app.config.from_prefixed_env()
log = app.logger

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_valid_time(time_str):
    try:
        datetime.strptime(time_str, '%H:%M:%S')
        return True
    except ValueError:
        return False



@app.route("/", methods=("GET",))
def lista_clinicas():
    """Lista todas as clínicas (nome e morada)."""

    with pool.connection() as conn:
        with conn.cursor() as cur:
            clinicas = cur.execute(
                """
                SELECT
                    nome, morada
                FROM
                    clinica;
                """,
                {},
            ).fetchall()

    return jsonify(clinicas)


@app.route("/c/<clinica>/", methods=("GET",))
def lista_especialidades(clinica):
    """Lista todas as especialidades oferecidas na <clinica>."""

    with pool.connection() as conn:
        with conn.cursor() as cur:
            
            # Verificar se a clínica existe
            existe_clinica = cur.execute(
                """
                SELECT c.nome
                FROM clinica c
                WHERE c.nome = %(clinica)s
                """,
                {"clinica": clinica}
            ).fetchone()
            if not existe_clinica:
                return jsonify({"Erro": "Clínica não existe!"}), 404

            # Obter todas as especialidades para a clínica
            especialidades = cur.execute(
                """
                SELECT
                    especialidade
                FROM
                    clinica c
                JOIN 
                    trabalha t USING (nome)
                JOIN
                    medico m USING (nif)
                WHERE 
                    c.nome = %(nome)s
                GROUP BY 
                    especialidade
                """,
                {"nome": clinica},
            ).fetchall()

    return jsonify(especialidades)


@app.route("/c/<clinica>/<especialidade>/", methods=("GET",))
def lista_medicos_especialidade(clinica, especialidade):
    """Lista todos os médicos (nome) da <especialidade> que trabalham na <clinica> e os
    primeiros três horários disponíveis para consulta de cada um deles (data e hora)."""

    with pool.connection() as conn:
        with conn.cursor() as cur:

            # Verificar se a clínica existe
            existe_clinica = cur.execute(
                """
                SELECT c.nome
                FROM clinica c
                WHERE c.nome = %(clinica)s
                """,
                {"clinica": clinica}
            ).fetchone()

            if not existe_clinica:
                return jsonify({"Erro": "Clínica não existe!"}), 404

            # Verificar se a especialidade existe
            existe_especialidade = cur.execute(
                """
                SELECT m.especialidade
                FROM medico m
                    JOIN trabalha t ON t.nif = m.nif
                    JOIN clinica c ON c.nome = t.nome
                WHERE m.especialidade = %(especialidade)s
                """,
                {"especialidade": especialidade},
            ).fetchone()
            if not existe_especialidade:
                return jsonify({"Erro": "Esta especialidade não existe nesta clinica!"}), 404

            # Obter os 3 próximos horários de disponibilidade para cada médico (na clínica)
            consultas = cur.execute(
                """
                    WITH horarios_disponiveis AS (
                        SELECT 
                            m.nome AS medico,
                            hp.data AS data,
                            hp.horario AS horario,
                            m.nif AS medico_nif
                        FROM 
                            horarios hp
                        JOIN 
                            trabalha tr ON EXTRACT(DOW FROM hp.data) = tr.dia_da_semana
                        JOIN 
                            medico m ON m.nif = tr.nif
                        LEFT JOIN 
                            consulta c ON hp.data = c.data AND hp.horario = c.hora AND c.nif = tr.nif
                        WHERE 
                            c.data IS NULL
                            AND m.especialidade = %(especialidade)s
                            AND tr.nome = %(clinica)s
                            AND (hp.data + hp.horario::interval) >= (NOW() + INTERVAL '1 hour')
                    )
                    SELECT hd.medico, hd.data, hd.horario
                    FROM horarios_disponiveis hd
                    WHERE (
                        SELECT COUNT(*)
                        FROM horarios_disponiveis hd2
                        WHERE hd2.medico = hd.medico
                        AND (hd2.data < hd.data OR (hd2.data = hd.data AND hd2.horario < hd.horario))
                    ) < 3
                    ORDER BY hd.medico, hd.data, hd.horario;
                """,
                {"clinica": clinica, "especialidade": especialidade},
            ).fetchall()
    
        # Criar dicionário com lista de horários por médico
        medicos = {}
        ultimo_medico = None
        medico = None
        for consulta in consultas:
            if consulta[0] != ultimo_medico:
                if medico != None: medicos[ultimo_medico] = medico
                medico = [str(consulta[1]) + " " + str(consulta[2])]
                ultimo_medico = consulta[0]
            else:
                medico.append(str(consulta[1]) + " " + str(consulta[2]))
        medicos[ultimo_medico] = medico

    return jsonify(medicos)



@app.route("/a/<clinica>/registar/", methods=("POST",))
def marcar_consulta(clinica):
    """Regista uma marcação de consulta na <clinica> na base de dados.
    Recebe como argumentos um paciente, um médico, e uma data e hora (posteriores ao momento de agendamento)."""
    paciente_ssn = request.args.get("paciente")
    medico_nif = request.args.get("medico")
    data = request.args.get("data")
    hora = request.args.get("hora")

    error = ""

    if not paciente_ssn:
        error = "Paciente em falta. "
    if not medico_nif:
        error += "Médico em falta. "
    if not data:
        error += "Data em falta. "
    if not hora:
        error += "Hora em falta."

    if error != "":
        return jsonify({"Argumento(s) em falta": error}), 400


    if not is_valid_date(data):
        return jsonify({"Erro": "Data fornecida não é uma data válida!"}), 400
    if not is_valid_time(hora):
        return jsonify({"Erro": "Hora fornecida não é uma hora válida!"}), 400


    with pool.connection() as conn:
        try:
            with conn.cursor() as cur:

                # Verificar se a clínica existe
                existe_clinica = cur.execute(
                    """
                    SELECT c.nome
                    FROM clinica c
                    WHERE c.nome = %(clinica)s
                    """,
                    {"clinica": clinica}
                ).fetchone()

                if not existe_clinica:
                    return jsonify({"Erro": "Clínica não existe."}), 404
            
                # Verificar se médico existe
                existe_medico = cur.execute(
                    """
                    SELECT 1
                    FROM medico
                    WHERE nif = %(medico_nif)s
                    """,
                    {"medico_nif": medico_nif},
                ).fetchone()

                if not existe_medico:
                    return jsonify({"Erro": "Médico não existe."}), 404
                
                # Verifica se paciente está na base de dados
                existe_paciente = cur.execute(
                    """
                    SELECT 1
                    FROM paciente p
                    WHERE p.ssn = %(paciente_ssn)s;
                    """,
                    {"paciente_ssn": paciente_ssn}
                ).fetchone()

                if not existe_paciente:
                    return jsonify({"Erro": "Paciente não está registado."}), 404
                
                # Verificar se a data e hora são posteriores ao momento atual
                horario_posterior = cur.execute(
                    """
                    SELECT 1
                    WHERE (%(data)s::date + %(hora)s::time) >= (NOW() + INTERVAL '1 hour')
                    """,
                    {"data": data, "hora": hora}
                ).fetchone()

                if not horario_posterior:
                    return  jsonify({"Erro": "Marcação deve ser posterior à data atual!"}), 400
                
                 # Verificar se médico trabalha na clínica no dia da semana pretendido
                medico_trabalha = cur.execute(
                    """
                    SELECT 1 FROM trabalha t
                    INNER JOIN medico m USING (nif)
                    WHERE m.nif = %(medico_nif)s AND t.nome = %(clinica)s AND t.dia_da_semana = EXTRACT(DOW FROM %(data)s::date);
                    """,
                    {"medico_nif": medico_nif, "clinica": clinica, "data": data},
                ).fetchone()

                if not medico_trabalha:
                    return jsonify({"Erro": "Médico não trabalha nesta clínica neste dia da semana."}), 400

                # Verifica se médico tem disponibilidade nesta data e hora
                medico_ocupado = cur.execute(
                    """
                    SELECT 1
                    FROM consulta c
                    WHERE c.data = %(data)s
                      AND c.hora = %(hora)s
                      AND c.nif = %(medico_nif)s;
                    """,
                    {"data": data, "hora": hora, "medico_nif": medico_nif}
                ).fetchone()
                
                if medico_ocupado:
                    return jsonify({"Erro": "Médico não tem disponibilidade neste horário."}), 400

                # Verificar se paciente tem disponibilidade (não está em nenhuma consulta a esta hora)
                cur.execute(
                    """
                    SELECT 1
                    FROM consulta c
                    WHERE c.ssn = %(paciente_ssn)s
                      AND c.data = %(data)s
                      AND c.hora = %(hora)s;
                    """,
                    {"paciente_ssn": paciente_ssn, "data": data, "hora": hora}
                )
                paciente_ocupado = cur.fetchone()
                if paciente_ocupado:
                    return jsonify({"Erro": "Paciente já tem uma consulta marcada para esta hora."}), 400

                # Se todas as verificações têm sucesso, registar consulta
                cur.execute(
                    """
                    INSERT INTO consulta (ssn, nif, nome, data, hora, codigo_sns)
                    VALUES (%(paciente_ssn)s, %(medico_nif)s, %(clinica)s, %(data)s, %(hora)s, NULL);
                    """,
                    {"paciente_ssn": paciente_ssn, "medico_nif": medico_nif, "clinica": clinica, "data": data, "hora": hora}
                )
                conn.commit()

        except psycopg.DatabaseError as e:
            # Rollback in case of error
            conn.rollback()
            error_message = str(e)
            if "right_schedule" in error_message:
                return jsonify({"Erro": "Hora fornecida para marcação de consulta não está de acordo com as diretrizes."}), 400
            elif "doctor_consulted_himself_func" in error_message:
                return jsonify({"Erro": "Médico não se pode consultar a si próprio!"}), 400
            
            #elif "doctor_wrong_clinic_func" in error_message:
            #    return "Médico não dá consultas nesta clinica neste dia da semana!", 400

            # É necessário isto ser verificado antes pois caso não fosse, não seria
            # possível distinguir este erro do erro de o horário do médico está indisponível
            else:
                return jsonify({"Erro": "DB error"}), 500

    return jsonify({"Sucesso": "Consulta registada com sucesso!"}), 200


@app.route("/a/<clinica>/cancelar/", methods=("POST",))
def cancelar_consulta(clinica):
    """Cancela uma marcação de consulta que ainda não se realizou na <clinica> (o seu horário é
    posterior ao momento do cancelamento), removendo a entrada da respectiva tabela na base de
    dados. Recebe como argumentos um paciente, um médico, e uma data e hora."""
    paciente_ssn = request.args.get("paciente")
    medico_nif = request.args.get("medico")
    data = request.args.get("data")
    hora = request.args.get("hora")

    error = ""

    if not paciente_ssn:
        error = "Paciente em falta. "
    if not medico_nif:
        error += "Médico em falta. "
    if not data:
        error += "Data em falta. "
    if not hora:
        error += "Hora em falta."

    if error != "":
        return jsonify({"Argumento(s) em falta": error}), 400


    if(not is_valid_date(data)):
        return jsonify({"Erro": "Data fornecida não é uma data válida."}), 400
    if(not is_valid_time(hora)):
        return jsonify({"Erro": "Hora fornecida não é uma hora válida!"}), 400

    with pool.connection() as conn:
        with conn.cursor() as cur:  

            # Verificar se a clínica existe
            existe_clinica = cur.execute(
                """
                SELECT c.nome
                FROM clinica c
                WHERE c.nome = %(clinica)s
                """,
                {"clinica": clinica}
            ).fetchone()

            if not existe_clinica:
                return jsonify({"Erro": "Clínica não existe."}), 404
        
            # Verificar se médico existe
            existe_medico = cur.execute(
                """
                SELECT 1
                FROM medico
                WHERE nif = %(medico_nif)s
                """,
                {"medico_nif": medico_nif},
            ).fetchone()

            if not existe_medico:
                return jsonify({"Erro": "Médico não existe."}), 404
            
            # Verifica se paciente está na base de dados
            existe_paciente = cur.execute(
                """
                SELECT 1
                FROM paciente p
                WHERE p.ssn = %(paciente_ssn)s;
                """,
                {"paciente_ssn": paciente_ssn}
            ).fetchone()

            if not existe_paciente:
                return jsonify({"Erro": "Paciente não está registado."}), 404
            
            # Verificar se a data e hora são posteriores ao momento atual
            horario_posterior = cur.execute(
                """
                SELECT 1
                WHERE (%(data)s::date + %(hora)s::time) >= (NOW() + INTERVAL '1 hour')
                """,
                {"data": data, "hora": hora}
            ).fetchone()

            if not horario_posterior:
                return jsonify({"Erro": "Não pode cancelar uma consulta que já passou."}), 400
            
            # Verificar se é um horário correto
            horario_correto = cur.execute(
                """
                SELECT 1
                FROM horarios
                WHERE 
                    data = %(data)s 
                    AND horario = %(hora)s
                """,
                {"data": data, "hora": hora},
            ).fetchone()

            if not horario_correto:
                return jsonify({"Erro": "Hora fornecida não está de acordo com as diretrizes."}), 400
            
            # Verificar se a consulta existe
            cur.execute(
                """
                SELECT id, codigo_sns FROM consulta
                WHERE 
                    nif = %(medico_nif)s
                    AND nome = %(clinica)s
                    AND ssn = %(paciente_ssn)s
                    AND data = %(data)s 
                    AND hora = %(hora)s;
                """,
                {"medico_nif": medico_nif, "paciente_ssn": paciente_ssn, "data": data, "hora": hora, "clinica": clinica},
            )
            consulta = cur.fetchone() # 0: id | 1: codigo_sns
            if not consulta:
                return jsonify({"Erro": "A consulta a cancelar não foi encontrada."}), 404

            # Eliminar observação e receita (dependentes da consulta)
            cur.execute(
                """
                DELETE FROM
                    observacao
                WHERE
                    id = %(id_consulta)s;
                """,
                {"id_consulta": consulta[0]},
            )
            cur.execute(
                """
                DELETE FROM
                    receita
                WHERE
                    codigo_sns = %(codigo_sns)s;
                """,
                {"codigo_sns": consulta[1]},
            )

            cur.execute(
                """
                DELETE FROM
                    consulta
                WHERE
                    id = %(id_consulta)s;
                """,
                {"id_consulta": consulta[0]},
            )

    return jsonify({"Sucesso": "Consulta cancelada com sucesso!"}), 200


if __name__ == "__main__":
    app.run()
