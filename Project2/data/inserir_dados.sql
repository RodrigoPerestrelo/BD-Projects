-- Apagar todos os dados existentes
DELETE FROM observacao;
DELETE FROM receita;
DELETE FROM consulta;
DELETE FROM paciente;
DELETE FROM trabalha;
DELETE FROM medico;
DELETE FROM enfermeiro;
DELETE FROM clinica;

-- Reset da sequência dos ids (para consultas)
SELECT setval('consulta_id_seq', 1, false);

-- Inserir os dados a partir dos ficheiros .txt
\COPY clinica(nome, telefone, morada) FROM 'clinicas.txt' DELIMITER ';' CSV HEADER;
\COPY enfermeiro(nif, nome, telefone, morada, nome_clinica) FROM 'enfermeiros.txt' DELIMITER ';' CSV HEADER;
\COPY medico(nif, nome, telefone, morada, especialidade) FROM 'medicos.txt' DELIMITER ';' CSV HEADER;
\COPY trabalha(nif, nome, dia_da_semana) FROM 'trabalha.txt' DELIMITER ';' CSV HEADER;
\COPY paciente(ssn, nif, nome, telefone, morada, data_nasc) FROM 'pacientes.txt' DELIMITER ';' CSV HEADER;
\COPY consulta(id, ssn, nif, nome, data, hora, codigo_sns) FROM 'consultas.txt' DELIMITER ';' CSV HEADER;
\COPY receita(codigo_sns, medicamento, quantidade) FROM 'receitas.txt' DELIMITER ';' CSV HEADER;
\COPY observacao(id, parametro, valor) FROM 'observacoes.txt' DELIMITER ';' CSV HEADER;

-- Update da sequência de id para consultas (não é automático com \COPY)
DO $$
DECLARE
    max_id INTEGER;
BEGIN
    SELECT MAX(id) INTO max_id FROM consulta;
    IF max_id IS NOT NULL THEN
        EXECUTE 'ALTER SEQUENCE consulta_id_seq RESTART WITH ' || (max_id + 1);
    END IF;
END $$;