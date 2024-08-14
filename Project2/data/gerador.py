import random
import datetime
import csv

# Lista de nomes e apelidos expandida
nomes = ["João", "Maria", "Pedro", "Ana", "Luís", "Margarida", "Carlos", "Teresa", "Manuel", "Rita", 
         "José", "Sofia", "António", "Filipa", "Francisco", "Catarina", "Rui", "Andreia", "Miguel", "Inês",
         "Daniel", "Beatriz", "Joaquim", "Diana", "David", "Cristina", "Hugo", "Isabel", "Bruno", "Patrícia",
         "Nuno", "Andreia", "Paulo", "Carla", "Ricardo", "Sara", "Jorge", "Sónia", "Fernando", "Tânia", "Eduardo",
         "Vera", "Alberto", "Helena", "Leonor", "Raul", "Simone", "Fábio", "Vânia", "Vasco", "Ana Luísa",
         "Amélia", "Fernanda", "Simão", "Tatiana", "Artur", "Marisa", "Gonçalo", "Carolina", "Hélder", "Lara",
         "Josué", "Viviane", "Hélio", "Liliana", "Júlio", "Andreia", "Kevin", "Daniela", "Leonardo", "Vanessa",
         "Dinis", "Rosa", "Júlia", "Jacinto", "Mónica", "Jéssica", "Bianca", "Íris", "Eva", "Eduarda", "Júlia"]

apelidos = ["Silva", "Santos", "Pereira", "Ferreira", "Oliveira", "Rodrigues", "Martins", "Sousa", "Fernandes",
            "Gomes", "Lopes", "Marques", "Almeida", "Alves", "Ribeiro", "Pinto", "Carvalho", "Teixeira", "Costa",
            "Mendes", "Nunes", "Correia", "Figueiredo", "Henriques", "Duarte", "Barbosa", "Freitas", "Rocha",
            "Pires", "Monteiro", "Moreira", "Cardoso", "Fonseca", "Araújo", "Piedade", "Cruz", "Reis", "Machado",
            "Miranda", "Gaspar", "Jesus", "Vieira", "Correia", "Brito", "Neves", "Maia", "Santana", "Lourenço",
            "Quaresma", "Santiago", "Melo", "Moura", "Gonçalves", "Matos", "Simões", "Abreu", "Amorim", "Vaz",
            "Leal", "Ramos", "Borges", "Tavares", "Rosa", "Silveira", "Paulino", "Cabral", "Braga", "Valente",
            "Cunha", "Pereirinha", "Pinheiro", "Mota", "Pacheco", "Paiva", "Baptista", "Brito", "Machado",
            "Estevão", "Madeira", "Batista", "Caldeira", "Branco", "Pessoa", "Bento", "Cordeiro", "Teles"]

# Lista de ruas e cidades expandida
streets = ["Rua das Flores", "Avenida Central", "Travessa da Esperança", "Praça da Liberdade",
           "Rua dos Cedros", "Avenida da República", "Travessa das Oliveiras", "Praça do Comércio",
           "Rua dos Pinheiros", "Avenida dos Aliados", "Travessa das Rosas", "Praça de Espanha",
           "Rua das Amendoeiras", "Avenida dos Descobrimentos", "Travessa dos Lírios", "Praça da Sé",
           "Rua das Margaridas", "Avenida das Acácias", "Travessa das Papoilas", "Praça do Marquês",
           "Rua dos Girassóis", "Avenida da Praia", "Travessa do Sol", "Praça da Paz",
            "Rua das Oliveiras", "Avenida dos Pássaros", "Travessa do Ouro", "Praça da Alegria",
            "Rua das Palmeiras", "Avenida das Rosas", "Travessa do Mar", "Praça do Amor",
            "Rua das Violetas", "Avenida dos Ventos", "Travessa das Estrelas", "Praça da Harmonia",
            "Rua dos Cravos", "Avenida da Lua", "Travessa da Felicidade", "Praça da Serenidade",
            "Rua das Orquídeas", "Avenida das Águias", "Travessa do Horizonte", "Praça do Sonho",
            "Rua dos Jasmins", "Avenida dos Oceanos", "Travessa das Marés", "Praça dos Sonhos",
            "Rua das Tulipas", "Avenida da Montanha", "Travessa do Bosque", "Praça das Ilusões",
            "Rua dos Narcisos", "Avenida das Colinas", "Travessa dos Rios", "Praça dos Desejos",
            "Rua das Magnólias", "Avenida das Fontes", "Travessa das Sombras", "Praça das Estrelas"
        ]

# Cidades onde possam existir moradas para pacientes
cities = ["Lisboa", "Porto", "Braga", "Faro",
          "Amadora", "Vila Nova de Gaia", "Coimbra", "Setúbal",
          "Sintra", "Bragança", "Évora", "Viana do Castelo",
          "Cascais", "Guimarães", "Leiria", "Funchal", "Almada", "Oeiras"]

# Cidades onde possam existir clinicas
clinic_cities = ["Lisboa", "Almada", "Cascais", "Oeiras", "Sintra"]

# Correspondencia da cidade com a Clinica (Isto para que os enfermeiros vivam
# na mesma cidade em que trabalham)
clinics = {
    "Lisboa": "Clinica Lisboa Central",
    "Almada": "Clinica Almada Saúde",
    "Cascais": "Clinica Cascais Bem-Estar",
    "Oeiras": "Clinica Oeiras Saúde",
    "Sintra": "Clinica Sintra Cuidados"
}
clinics_lista = ["Clinica Lisboa Central", "Clinica Almada Saúde", "Clinica Cascais Bem-Estar", "Clinica Oeiras Saúde", "Clinica Sintra Cuidados"]

# Dicionário de códigos postais correspondentes às cidades
postal_codes_dict = {
    "Lisboa": ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19"],
    "Porto": ["40", "41", "42", "43"],
    "Braga": ["47", "48", "49", "50"],
    "Faro": ["80", "81", "82", "83"],
    "Amadora": ["2650"],
    "Almada": ["28"],
    "Vila Nova de Gaia": ["44", "45", "46", "47"],
    "Coimbra": ["30", "31", "32", "33"],
    "Setúbal": ["29", "29", "29", "29"],
    "Sintra": ["2710", "2711", "2712", "2713", "2714", "2715"],
    "Bragança": ["53", "54", "55", "56"],
    "Évora": ["70", "71", "72", "73"],
    "Viana do Castelo": ["49", "49", "49", "49"],
    "Cascais": ["2645", "2646", "2647", "2648" , "2649"],
    "Guimarães": ["48", "48", "48", "48"],
    "Leiria": ["24", "24", "24", "24"],
    "Funchal": ["90", "91", "92", "93"],
    "Oeiras": ["2780"]
}

# Listas para armazenar números já utilizados
telefones_usados = []
ssn_usados = []
nif_usados = []
moradas_usadas = []

def calcular_dia_semana(data):

    ano, mes, dia = map(int, data.split('-'))

    if mes < 3:
        mes += 12
        ano -= 1
    K = ano % 100
    J = ano // 100
    f = dia + ((13 * (mes + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)
    dia_semana = f % 7

    return (dia_semana + 6) % 7

# Função para gerar um SSN (Número de Seguro Social) único
def generate_ssn():
    ssn = ''.join(random.choices('0123456789', k=11))
    while ssn in ssn_usados:
        ssn = ''.join(random.choices('0123456789', k=11))
    ssn_usados.append(ssn)
    return ssn

# Função para gerar um NIF (Número de Identificação Fiscal) único
def generate_nif():
    nif = ''.join(random.choices('0123456789', k=9))
    while nif in nif_usados:
        nif = ''.join(random.choices('0123456789', k=9))
    nif_usados.append(nif)
    return nif

# Função para gerar um número de telefone único
def generate_phone_number():
    phone_number = '9' + ''.join(random.choices('0123456789', k=8))
    while phone_number in telefones_usados:
        phone_number = '9' + ''.join(random.choices('0123456789', k=8))
    telefones_usados.append(phone_number)
    return phone_number

# Função para gerar uma morada única
def generate_address(city):
    street = random.choice(streets)
    if(city == "Random"):
        city = random.choice(cities)
    postal_code_prefix = random.choice(postal_codes_dict[city])
    if len(postal_code_prefix) == 2:
        postal_code_prefix = postal_code_prefix + ''.join(random.choices('0123456789', k=2))
    postal_code_suffix = ''.join(random.choices('0123456789', k=3))
    postal_code = f"{postal_code_prefix}-{postal_code_suffix}"
    address = f"{street}, {random.randint(1, 100)}, {postal_code} {city}"
    while address in moradas_usadas:
        street = random.choice(streets)
        city = random.choice(cities)
        postal_code_prefix = random.choice(postal_codes_dict[city])
        if len(postal_code_prefix) == 2:
            postal_code_prefix = postal_code_prefix + ''.join(random.choices('0123456789', k=2))
        postal_code_suffix = ''.join(random.choices('0123456789', k=3))
        postal_code = f"{postal_code_prefix}-{postal_code_suffix}"
        address = f"{street}, {random.randint(1, 100)}, {postal_code} {city}"
    moradas_usadas.append(address)
    return address


# Função para gerar uma data de nascimento
def generate_birth_date():
    start_date = datetime.date(1950, 1, 1)
    end_date = datetime.date(2023, 12, 31) # Restrição: datas de nascimento até 2023
    return start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))



# Geração dos enfermeiros
faz_instancia_enfermeiro = [] # Lista com todas as instâncias de enfermeiros
nomes_enfermeiros = [] # Para não repetir nomes de enfermeiros
j = 0

# Cada clinica tem 6 enfermeiros
for city in clinic_cities:
    while (j < 6):
        nif = generate_nif()
        nome = f"{random.choice(nomes)} {random.choice(apelidos)}"
        while nome in nomes_enfermeiros:
            nome = f"{random.choice(nomes)} {random.choice(apelidos)}"
        nomes_enfermeiros.append(nome)
        phone_number = generate_phone_number()
        address = generate_address(city)
        faz_instancia_enfermeiro.append((nif, nome, phone_number, address, clinics[city]))
        j += 1
    j = 0



# Geração do médicos
medicos_cardiologia = []

faz_instancia_medico = [] # Lista com todos os medicos
nomes_medicos = [] # Para não repetir nomes de médicos
nifs_medicos = [] # Nifs dos médicos existentes

num_ortopedia = random.randint(1, 7) # Número de médicos ortopedistas
num_cardiologia = random.randint(1, 7) # Número de médicos cardiologistas

outras_especialidades = ["Ginecologia", "Dermatologia", "Pediatria"]

for i in range(60):
    nif = generate_nif()
    nifs_medicos.append(nif)
    nome = f"{random.choice(nomes)} {random.choice(apelidos)}"
    while nome in nomes_medicos:
        nome = f"{random.choice(nomes)} {random.choice(apelidos)}"
    nomes_medicos.append(nome)
    phone_number = generate_phone_number()
    city = random.choice(clinic_cities)
    address = generate_address(city)
    if (i < 20):
        especialidade = "Clinica Geral"
    elif (i < 20 + num_ortopedia):
        especialidade = "Ortopedia"
    elif (i < 20 + num_ortopedia + num_cardiologia):
        especialidade = "Cardiologia"
    else:
        especialidade = random.choice(outras_especialidades)
    faz_instancia_medico.append((nif, nome, phone_number, address, especialidade))
    if (especialidade == "Cardiologia"):
        medicos_cardiologia.append((nif, nome, phone_number, address, especialidade))



# Gerar pacientes

faz_instancia_paciente = [] # Lista com todos os pacientes

for _ in range(5000):
    nome = f"{random.choice(nomes)} {random.choice(apelidos)}"
    ssn = generate_ssn()
    nif = generate_nif()
    phone_number = generate_phone_number()
    address = generate_address("Random")
    birth_date = generate_birth_date().strftime("'%Y-%m-%d'")
    faz_instancia_paciente.append((ssn, nif, nome, phone_number, address, birth_date))



# Coisas necessárias para as consultas e para os médicos
# O que está comentado com """ """ são o que existe nas variáveis diretamente abaixo


"""
    "{
        'NIF': {'0': [Clinica 1], '1': [Clinica 1]}
        'NIF': {'0': [Clinica 1], '1': []}
    }"
"""
medico_dow_clinica = {}

for nif in nifs_medicos:
    medico_dow_clinica[nif] = {dia: [] for dia in range(7)}



"""
    "{
        'Clinica 1': {'0': [Médico 1, Médico 2, etc], '1': [Médico 3, Médico 4, etc]}
    }"
"""
clinica_dow_medicos = {}

for city in clinic_cities:
    clinica_dow_medicos[clinics[city]] = {dia: [] for dia in range(7)}



"""
    "{
        '1': [Médico 1, Médico 2, etc]
        '2': [Médico 1, Médico 3, etc]
    }"
"""
dow_medicos = {dia: [] for dia in range(7)}



"""
    "{
        'NIF': [Clinica 1, Clinica 1, Clinica 1]
    }"
"""
medico_clinica = {}

for nif in nifs_medicos:
    medico_clinica[nif] = []



"""
    "{
        'NIF': [Clinica 1] (mesmo que o de cima, só que sem repetidos)
    }"
"""
medico_clinica_unico = {}

for nif in nifs_medicos:
    medico_clinica_unico[nif] = []


# Coloca o minimo de 8 médicos por clinica, por dia

for day in range(7):
    for city in clinic_cities:
        for numMedicos in range(8):
            nif_medico = random.choice(nifs_medicos)
            # Garante que um médico não trabalha em dois sitios diferentes no mesmo dia e que não trabalha mais de 6 dias
            while(nif_medico in dow_medicos[day] or len(medico_clinica[nif_medico]) >= 6):
                nif_medico = random.choice(nifs_medicos)
            
            dow_medicos[day].append(nif_medico) # Médicos a trabalhar naquele dia
            medico_clinica[nif_medico].append(clinics[city]) # Clinicas a que o médico trabalha (cada indice é um dia e tem a clinica onde está a trabalhar no indice do dia)

            # Clinicas diferentes no qual o médico trabalha
            if (nif_medico not in medico_clinica_unico[nif_medico]):
                medico_clinica_unico[nif_medico].append(clinics[city])

            # Por médico, por dia, em que Clinica é que trabalha
            medico_dow_clinica[nif_medico][day].append(clinics[city])
            # Por clinica, por dia, que médico trabalham lá
            clinica_dow_medicos[clinics[city]][day].append(nif_medico)


# Coloca os médicos que só trabalham em uma clinica a trabalhar em mais uma pelo menos
# num dia em que já não estejam a trabalhar e numa clinica que ainda não trabalhassem
for nif in nifs_medicos:
    if(len(medico_clinica_unico[nif]) < 2):
        city = random.choice(clinic_cities)
        clinic = clinics[city]
        day = random.randint(0, 6)
        # Enquanto não encontrar um dia em que o médico não esteja a trabalhar ou enquanto a clinica for a mesma da que ele já trabalha
        while(nif in dow_medicos[day] or (clinic in medico_clinica_unico[nif])):
            city = random.choice(clinic_cities)
            clinic = clinics[city]
            day = random.randint(0, 7)

        dow_medicos[day].append(nif) # Médicos a trabalhar naquele dia
        medico_clinica[nif].append(clinic) # Clinicas a que o médico trabalha (cada indice é um dia e tem a clinica onde está a trabalhar no indice do dia)
        medico_clinica_unico[nif].append(clinics[city]) # Clinicas diferentes no qual o médico trabalha
        medico_dow_clinica[nif][day].append(clinics[city]) # Por médico, por dia, em que Clinica é que trabalha
        clinica_dow_medicos[clinic][day].append(nif) # Por clinica, por dia, que médicos trabalham lá

# Se um médico não trabalha 7 dias por semana, coloca-o a trabalhar todos os dias
for nif in nifs_medicos:
    if (len(medico_clinica[nif]) < 7):
        for day in range(7):
            if (nif not in dow_medicos[day]):
                city = random.choice(clinic_cities)
                clinic = clinics[city]

                dow_medicos[day].append(nif) # Médicos a trabalhar naquele dia
                medico_clinica[nif].append(clinic) # Clinicas a que o médico trabalha (cada indice é um dia e tem a clinica onde está a trabalhar no indice do dia)
                medico_clinica_unico[nif].append(clinics[city]) # Clinicas diferentes no qual o médico trabalha
                medico_dow_clinica[nif][day].append(clinics[city]) # Por médico, por dia, em que Clinica é que trabalha
                clinica_dow_medicos[clinic][day].append(nif) # Por clinica, por dia, que médicos trabalham lá


faz_instancia_trabalha = [] # Lista com todas as instâncias de trabalha
for nif in nifs_medicos:
    for day in range(7):
        if(medico_dow_clinica[nif][day] != []):
            faz_instancia_trabalha.append((nif, medico_dow_clinica[nif][day][0], day))

#Parâmetros para as consultas
# Parâmetros Qualitativos
parametros_qualitativos_ = [
    "Aparência Geral do Paciente",
    "Postura Corporal",
    "Expressão Facial",
    "Nível de Conforto",
    "Tom de Voz",
    "Contato Visual",
    "Higiene Pessoal",
    "Comportamento Geral",
    "Movimentação",
    "Respiração",
    "Coloração da Pele",
    "Presença de Cicatrizes ou Lesões",
    "Textura da Pele",
    "Expressão Emocional",
    "Estado de Alerta",
    "Padrão de Fala",
    "Hálito",
    "Estado de Humor",
    "Atitude",
    "Nível de Energia",
    "Interação Social",
    "Confiança",
    "Uso de Acessórios",
    "Vestimenta",
    "Relação com o Médico",
    "Memória",
    "Orientação no Tempo e Espaço",
    "Coordenação Motora",
    "Presença de Tiques",
    "Manchas na Pele",
    "Habilidades de Comunicação",
    "Motivação",
    "Reação ao Toque",
    "Temperamento",
    "Consciência Corporal",
    "Dedos e Unhas",
    "Interesse na Consulta",
    "Autonomia",
    "Suporte Familiar",
    "Estabilidade Emocional",
    "Cicatrização de Feridas",
    "Evidências de Abuso",
    "Nível de Estresse",
    "Habilidades Cognitivas",
    "Capacidade de Seguir Instruções",
    "Interesse pela Própria Saúde",
    "Nível de Hidatação",
    "Movimentos Anormais",
    "Sinais de Infecção",
    "Pele Moteada"
]
# Parâmetros Quantitativos
parametros_quantitativos_ = [
    "Altura (cm)",
    "Peso (kg)",
    "Pressão Arterial Sistólica (mmHg)",
    "Pressão Arterial Diastólica (mmHg)",
    "Frequência Cardíaca (bpm)",
    "Temperatura Corporal (°C)",
    "Índice de Massa Corporal (IMC)",
    "Nível de Glicose no Sangue (mg/dL)",
    "Nível de Colesterol Total (mg/dL)",
    "Nível de Triglicerídeos (mg/dL)",
    "Saturação de Oxigênio (%)",
    "Taxa de Filtração Glomerular (mL/min/1,73m²)",
    "Nível de Hemoglobina (g/dL)",
    "Contagem de Glóbulos Brancos (células/μL)",
    "Contagem de Plaquetas (milhares/μL)",
    "Nível de Creatinina Sérica (mg/dL)",
    "Volume Expiratório Forçado em 1 segundo (FEV1) (L)",
    "Capacidade Vital Forçada (FVC) (L)",
    "Ritmo Respiratório (respirações/min)",
    "Circunferência Abdominal (cm)"
]

# Temos 5 clinica
# Temos o trabalha com onde cada médico trabalha a cada dia da semana
# Eles têm de dar no mínimo 2 consultas por dia

# Lista com os pacientes que já foram consultados por um médico
pacientes_consultados = []
id_consulta = 0

# Lista com as consultas
faz_instancia_consulta = [] # (id_unico, ssn_paciente, nif_medico, nome_clinica, data, hora, codigo_sns)
datas_consulta = []
datas_consulta_paciente = []
ssn_receitas = []

# A data da consulta tem de ser entre 2023 e 2024 e tem de ser no dia em que o médico está a trabalhar
# A hora de inicio da consulta tem de ser entre as 9h e as 12h30 e das 14h às 17h30h
# Uma consulta nunca pode ser no mesmo dia e hora que outra consulta

horarios_disponiveis = [
    "9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30",
    "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30"
]

# Gera as consultas do paciente do medico de cardiologia que vai ter o mesmo medicamento nas 12 consultas
paciente = random.choice(faz_instancia_paciente)
medico = random.choice(medicos_cardiologia)
mes_atual = 6
ano_atual = datetime.date.today().year
nif_medico = medico[0]
ssn_paciente = paciente[0]
lista_codigos_sns_cardiologia = []
data = datetime.date(2024, 6, 10)
dia_reset = 10

# procura a clinica e o dia da semana em que o medico trabalha
for trabalha in faz_instancia_trabalha:
        if (trabalha[0] == medico[0]):
            nome_clinica = trabalha[1]
            dia_da_semana = trabalha[2]
            #print(trabalha)
            break


# gera as 13 consultas
for i in range(13):
    id_consulta += 1
    horario = random.choice(horarios_disponiveis)

    # gera um codigo_sns para a receita
    codigo_sns = ''.join(random.choices('0123456789', k=12))
    while codigo_sns in ssn_receitas:
        codigo_sns = ''.join(random.choices('0123456789', k=12))
    lista_codigos_sns_cardiologia.append(codigo_sns)
    ssn_receitas.append(codigo_sns)

    #gera um dia aleatorio para a consulta em 2024 no mes 05 mas no dia da semana que o medico trabalha
    while (calcular_dia_semana(data.strftime("%Y-%m-%d")) != dia_da_semana):
        # data = data menos um dia
        data = data - datetime.timedelta(days=1)
        #print(data)
    dia_atual = data.day

    data_inserir = datetime.date(ano_atual, mes_atual, dia_atual)
    data_convertido = data_inserir.strftime("%Y-%m-%d")
    datas_consulta.append((data_convertido, horario, nif_medico))

    #print(id_consulta, ssn_paciente, nif_medico, nome_clinica, data_convertido, horario, codigo_sns)
    faz_instancia_consulta.append((id_consulta,ssn_paciente, nif_medico, nome_clinica, data_convertido, horario, codigo_sns))
    mes_atual -= 1
    # data passa a ser no dia 28 mas no mes anterior ao atual
    if mes_atual== 0:
        ano_atual -= 1
        mes_atual = 12
    data = datetime.date(ano_atual, mes_atual, dia_reset)


data_inicial = datetime.date(2023, 1, 1)
data_final = datetime.date(2024, 5, 31)
data_atual = data_inicial

data_clinica_medico = {}

while data_atual < data_final:
    dow = (data_atual.weekday() + 1) % 7
    data_str = data_atual.strftime('%Y-%m-%d')  # Converte a data para string no formato 'YYYY-MM-DD'
    data_clinica_medico[data_str] = {}

    for clinica in clinics_lista:
        data_clinica_medico[data_str][clinica] = {}

        for medico in clinica_dow_medicos[clinica][dow]:
            data_clinica_medico[data_str][clinica][medico] = []

    data_atual += datetime.timedelta(days=1)

data_atual = data_inicial


# Itera pelos dias
while data_atual < data_final:

    # Itera pelas clinicas
    for clinica in clinics_lista:
        contador_consultas_dia = 0
        
        # Obtém os médicos presentes numa clinica num determinado dia da semana
        medicos_na_clinica_no_dia = clinica_dow_medicos[clinica][(data_atual.weekday() + 1) % 7]

    # Para cada medico num dia da semana numa clinica
        for medico in medicos_na_clinica_no_dia:
            # Coloca duas consultas para cada medico por clinica por dia da semana
            for i in range(2):
                id_consulta += 1

                ssn_paciente = random.choice(faz_instancia_paciente)[0]
                nif_medico = medico
                nome_clinica = clinica
                data = data_atual.strftime("%Y-%m-%d")
                horario = random.choice(horarios_disponiveis)
                while (data, horario, nif_medico) in datas_consulta:
                    horario = random.choice(horarios_disponiveis)
                while ((data, horario, ssn_paciente) in datas_consulta_paciente):
                    ssn_paciente = random.choice(faz_instancia_paciente)[0]
                if ssn_paciente not in pacientes_consultados:
                    pacientes_consultados.append(ssn_paciente)
                datas_consulta_paciente.append((data, horario, ssn_paciente))
                datas_consulta.append((data, horario, nif_medico))
                codigo_sns = ""
                num = random.randint(0, 99)
                if (num  >= 20 and data_atual < datetime.date(2024, 6, 1)):
                    codigo_sns = ''.join(random.choices('0123456789', k=12))
                    while codigo_sns in ssn_receitas:
                        codigo_sns = ''.join(random.choices('0123456789', k=12))
                    ssn_receitas.append(codigo_sns)

                data_clinica_medico[data][nome_clinica][nif_medico].append(horario)
                faz_instancia_consulta.append((id_consulta,ssn_paciente, nif_medico, nome_clinica, data, horario, codigo_sns))
                contador_consultas_dia += 1
            
            if contador_consultas_dia < 20:
                for i in range(20 - contador_consultas_dia):
                    id_consulta += 1

                    ssn_paciente = random.choice(faz_instancia_paciente)[0]
                    nif_medico = random.choice(medicos_na_clinica_no_dia)
                    nome_clinica = clinica
                    data = data_atual.strftime("%Y-%m-%d")
                    horario = random.choice(horarios_disponiveis)
                    while (data, horario, nif_medico) in datas_consulta:
                        nif_medico = random.choice(medicos_na_clinica_no_dia)
                        horario = random.choice(horarios_disponiveis)
                    while ((data, horario, ssn_paciente) in datas_consulta_paciente):
                        ssn_paciente = random.choice(faz_instancia_paciente)[0]
                    if ssn_paciente not in pacientes_consultados:
                        pacientes_consultados.append(ssn_paciente)
                    datas_consulta_paciente.append((data, horario, ssn_paciente))
                    datas_consulta.append((data, horario, nif_medico))
                    codigo_sns = ""
                    num = random.randint(0, 99)
                    if (num  >= 20 and data_atual < datetime.date(2024, 6, 1)):
                        codigo_sns = ''.join(random.choices('0123456789', k=12))
                        while codigo_sns in ssn_receitas:
                            codigo_sns = ''.join(random.choices('0123456789', k=12))
                        ssn_receitas.append(codigo_sns)

                    data_clinica_medico[data][nome_clinica][nif_medico].append(horario)
                    faz_instancia_consulta.append((id_consulta,ssn_paciente, nif_medico, nome_clinica, data, horario, codigo_sns))
                    contador_consultas_dia += 1

    data_atual += datetime.timedelta(days=1)


for paciente in faz_instancia_paciente:
    if paciente[0] not in pacientes_consultados:
        id_consulta += 1
        ssn_paciente = paciente[0]
        data = random.choice(datas_consulta)[0]
        medico_clinica = random.choice(faz_instancia_trabalha)

        while (calcular_dia_semana(data) != medico_clinica[2]):
            data = random.choice(datas_consulta)[0]

        nif_medico = medico_clinica[0]
        nome_clinica = medico_clinica[1]
        horario = random.choice(horarios_disponiveis)
        while (data, horario, nif_medico) in datas_consulta:
            data = random.choice(datas_consulta)[0]
            medico_clinica = random.choice(faz_instancia_trabalha)

            while (calcular_dia_semana(data) != medico_clinica[2]):
                data = random.choice(datas_consulta)[0]

            nif_medico = medico_clinica[0]
            nome_clinica = medico_clinica[1]
            horario = random.choice(horarios_disponiveis)
        datas_consulta.append((data, horario, nif_medico))
        codigo_sns = ""
        num = random.randint(0, 99)
        if (num  >= 20 and data_atual < datetime.date(2024, 6, 1)):
            codigo_sns = ''.join(random.choices('0123456789', k=12))
            while codigo_sns in ssn_receitas:
                codigo_sns = ''.join(random.choices('0123456789', k=12))
            ssn_receitas.append(codigo_sns)
        
        faz_instancia_consulta.append((id_consulta,ssn_paciente, nif_medico, nome_clinica, data, horario, codigo_sns))

medicamentos_ = [
    "Paracetamol",
    "Ibuprofeno",
    "Ácido acetilsalicílico (AAS)",
    "Diclofenaco",
    "Naproxeno",
    "Cetoprofeno",
    "Nimesulida",
    "Amoxicilina",
    "Azitromicina",
    "Ciprofloxacina",
    "Doxiciclina",
    "Levofloxacina",
    "Claritromicina",
    "Cefalexina",
    "Ceftriaxona",
    "Clindamicina",
    "Metronidazol",
    "Sulfametoxazol + Trimetoprim",
    "Aciclovir",
    "Oseltamivir",
    "Zidovudina",
    "Lamivudina",
    "Efavirenz",
    "Ritonavir",
    "Hidroxicloroquina",
    "Ivermectina",
    "Albendazol",
    "Mebendazol",
    "Metformina",
    "Glibenclamida",
    "Gliclazida",
    "Insulina",
    "Levotiroxina",
    "Propiltiouracil",
    "Carbimazol",
    "Prednisona",
    "Hidrocortisona",
    "Dexametasona",
    "Betametasona",
    "Alopurinol",
    "Colchicina",
    "Furosemida",
    "Hidroclorotiazida",
    "Espironolactona",
    "Amilorida",
    "Atenolol",
    "Metoprolol",
    "Propranolol",
    "Enalapril",
    "Losartana",
    "Valsartana",
    "Amlodipino",
    "Nifedipino",
    "Verapamil",
    "Diltiazem",
    "Digoxina",
    "Amiodarona",
    "Atorvastatina",
    "Sinvastatina",
    "Rosuvastatina",
    "Fenofibrato",
    "Gemfibrozil",
    "Clopidogrel",
    "Varfarina",
    "Rivaroxabana",
    "Apixabana",
    "Dabigatrana",
    "Heparina",
    "Enoxaparina",
    "Omeprazol",
    "Pantoprazol",
    "Lansoprazol",
    "Ranitidina",
    "Famotidina",
    "Domperidona",
    "Metoclopramida",
    "Ondansetrona",
    "Loperamida",
    "Bisacodil",
    "Lactulose",
    "Polietilenoglicol",
    "Simeticona",
    "Colecalciferol (Vitamina D)",
    "Retinol (Vitamina A)",
    "Ácido ascórbico (Vitamina C)",
    "Tocoferol (Vitamina E)",
    "Fitoesterol (Vitamina K)",
    "Tiamina (Vitamina B1)",
    "Riboflavina (Vitamina B2)",
    "Niacina (Vitamina B3)",
    "Piridoxina (Vitamina B6)",
    "Cianocobalamina (Vitamina B12)",
    "Ácido fólico",
    "Cloreto de sódio (soro fisiológico)",
    "Ringer lactato",
    "Glucose (dextrose)",
    "Noradrenalina",
    "Adrenalina",
    "Dopamina",
    "Dobutamina",
    "Nitroprussiato de sódio",
    "Nitroglicerina",
    "Isossorbida",
    "Fentanil",
    "Morfina",
    "Tramadol",
    "Codeína",
    "Hidromorfona",
    "Oxicodona",
    "Metadona",
    "Buprenorfina",
    "Naloxona",
    "Diazepam",
    "Lorazepam",
    "Clonazepam",
    "Alprazolam",
    "Midazolam",
    "Bromazepam",
    "Fluoxetina",
    "Sertralina",
    "Paroxetina",
    "Citalopram",
    "Escitalopram",
    "Amitriptilina",
    "Nortriptilina",
    "Venlafaxina",
    "Duloxetina",
    "Bupropiona",
    "Haloperidol",
    "Risperidona",
    "Olanzapina",
    "Quetiapina",
    "Aripiprazol",
    "Lítio",
    "Ácido valproico",
    "Carbamazepina",
    "Lamotrigina",
    "Gabapentina",
    "Pregabalina",
    "Topiramato",
    "Levetiracetam",
    "Fenitoína",
    "Cloridrato de betahistina",
    "Meclizina",
    "Dimenidrinato",
    "Bromoprida",
    "Cinarizina",
    "Buspirona",
    "Zolpidem",
    "Succinato de doxilamina"
]
# Receitas
# (codigo_sns, medicamento, quantidade)
faz_instancia_receitas = []

for consulta in faz_instancia_consulta:
    if consulta[6] != "":
        if consulta[6] in lista_codigos_sns_cardiologia:
            num_medicamentos = 1
            medicamento = "Ibuprofeno"
            quantidade = 3
            faz_instancia_receitas.append((consulta[6], medicamento, quantidade))
        else:
            num_medicamentos = random.randint(1, 6)
            medicamentos = []
            for _ in range(num_medicamentos):
                num = random.randint(0, 149)
                medicamento = medicamentos_[num]
                while medicamento in medicamentos:
                    num = random.randint(0, 149)
                    medicamento = medicamentos_[num]
                medicamentos.append(medicamento)
                quantidade = random.randint(1, 3)
                faz_instancia_receitas.append((consulta[6], medicamento, quantidade))

# Observações
# (id_consulta, medicamento, quantidade)
faz_instancia_observacoes = []

for consulta in faz_instancia_consulta:

    # se não for uma consulta com data posterior a 2024-06-01

    data_consulta_str = consulta[4]
    ano_consulta = int(data_consulta_str.split('-')[0])
    mes_consulta = int(data_consulta_str.split('-')[1])
    dia_consulta = int(data_consulta_str.split('-')[2])
    data_consulta = datetime.date(ano_consulta, mes_consulta, dia_consulta)

    if data_consulta < datetime.date(2024, 6, 1):
        parametros_qualitativos = []
        parametros_quantitativos = []

        num_observacoes_qualitativas = random.randint(1, 5)
        for _ in range(num_observacoes_qualitativas):
            
            num = random.randint(0, 49)
            parametro = parametros_qualitativos_[num]
            while parametro in parametros_qualitativos:
                num = random.randint(0, 49)
                parametro = parametros_qualitativos_[num]
            parametros_qualitativos.append(parametro)

            faz_instancia_observacoes.append((consulta[0], parametro, ''))

        num_observacoes_quantitativas = random.randint(0, 3)
        for _ in range(num_observacoes_quantitativas):

            num = random.randint(0, 19)
            parametro = parametros_quantitativos_[num]
            while parametro in parametros_quantitativos:
                num = random.randint(0, 19)
                parametro = parametros_quantitativos_[num]
            parametros_quantitativos.append(parametro)

            valor = random.uniform(0.1, 100)
            faz_instancia_observacoes.append((consulta[0], parametro, valor))


# Verificações de erros:

# Colocar depois todas as restrições existentes no enunciado e verificar
# se alguma delas é quebrada

# Clinicas por médico, cada indice corresponde a um dia da semana
data_atual = data_inicial
while data_atual < data_final:
    # n_consultas_dia = 0
    dow = (data_atual.weekday() + 1) % 7
    data_str = data_atual.strftime('%Y-%m-%d')  # Converte a data para string no formato 'YYYY-MM-DD'
    for clinica in clinics_lista:
        n_consultas = 0
        for medico in clinica_dow_medicos[clinica][dow]:
            n_consultas += len(data_clinica_medico[data_str][clinica][medico])
            if(len(data_clinica_medico[data_str][clinica][medico]) < 2):
                print("Médico tem menos de 2 consultas!")
        if(n_consultas < 20):
            print("Clinica tem menos de 20 consultas!")
        # n_consultas_dia += n_consultas
    # print("Tivemos ", n_consultas_dia, " no dia ", data_str)

    data_atual += datetime.timedelta(days=1)

for nif in nifs_medicos:
    if(len(medico_clinica_unico[nif]) < 2):
        print("Médico trabalha em menos de 0 ou 1 Clinica por semana!")

# Médicos por clinica por dia
for city in clinic_cities:
    for day in range(7):
        if(len(clinica_dow_medicos[clinics[city]][day]) < 8):
            print("A clinica tem menos de 8 médicos a trabalhar neste dia!") 

for nif in nifs_medicos:
    for day in range(7):
        if (len(medico_dow_clinica[nif][day]) > 1):
            print("Médico trabalha em mais de uma clinica num dia!")


# Escrever os dados gerados para ficheiros CSV

# Clinicas
with open('clinicas.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    arquivo_csv.write("nome;telefone;morada\n")
    arquivo_csv.write("Clinica Lisboa Central;213456789;Rua da Saúde, 123, 1000-001 Lisboa\n")
    arquivo_csv.write("Clinica Almada Saúde;212345678;Avenida Principal, 456, 2800-002 Almada\n")
    arquivo_csv.write("Clinica Cascais Bem-Estar;214567890;Rua da Praia, 789, 2750-003 Cascais\n")
    arquivo_csv.write("Clinica Oeiras Saúde;215678901;Avenida das Flores, 321, 2780-004 Oeiras\n")
    arquivo_csv.write("Clinica Sintra Cuidados;219012345;Largo da Paz, 654, 2710-005 Sintra\n")
# Enfermeiros
with open('enfermeiros.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    escritor_csv.writerow(["nif", "nome", "telefone", "morada", "nome_clinica"])
    for enfermeiro in faz_instancia_enfermeiro:
        escritor_csv.writerow(enfermeiro)
# Médicos
with open('medicos.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    escritor_csv.writerow(["nif", "nome", "telefone", "morada", "especialidade"])
    for medico in faz_instancia_medico:
        escritor_csv.writerow(medico)
# Pacientes
with open('pacientes.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    escritor_csv.writerow(["ssn", "nif", "nome", "telefone", "morada", "data_nasc"])
    for paciente in faz_instancia_paciente:
        escritor_csv.writerow(paciente)
# Trabalha
with open('trabalha.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    escritor_csv.writerow(["nif", "nome_clinica", "dia_da_semana"])
    for trabalha in faz_instancia_trabalha:
        escritor_csv.writerow(trabalha)
# Consultas
with open('consultas.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    escritor_csv.writerow(["id_unico", "ssn", "nif", "nome_clinica", "data", "hora", "codigo_sns"])
    for consulta in faz_instancia_consulta:
        escritor_csv.writerow(consulta)
# Receitas
with open('receitas.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    escritor_csv.writerow(["codigo_sns", "medicamento", "quantidade"])
    for receita in faz_instancia_receitas:
        escritor_csv.writerow(receita)
# Observações
with open('observacoes.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    escritor_csv.writerow(["id_consulta", "parametro", "valor"])
    for observacao in faz_instancia_observacoes:
        escritor_csv.writerow(observacao)
