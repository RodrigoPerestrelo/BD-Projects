-- Descrição: Testa pacientes com consultas em diversas clínicas, com o mesmo intervalo temporal
-- máximo entre duas observações do mesmo sintoma. 
-- Para além disso é adicionado outro sintoma para um dos pacientes. Este sintoma (como não ocorre
-- mais vezes) deve ser ignorado.
-- É ainda adicionado outro médico de uma especialidade diferente de 'Ortopedia' que regista o
-- mesmo sintoma para um dos pacientes (com um intervalo superior). Este sintoma (por não ser do)
-- foro ortopédico deve ser ignorado.
-- OUTPUT:
-- 22935155532
-- 22935155534

INSERT INTO clinica (nome, telefone, morada) VALUES
	('Clinica Lisboa Central', '213456789', 'Rua da Saúde, 123, 1000-001 Lisboa'),
    ('Clinica Almada Saúde', '212451421', 'Rua da Amendoeira, 13, 1023-018 Almada');

INSERT INTO medico (nif, nome, telefone, morada, especialidade) VALUES 
    ('350859354', 'António', '935810678', 'Praça da Alegria, 41, 2649-045 Cascais', 'Ortopedia'),
    ('350859326', 'Francisco', '935810678', 'Praça da Alegria, 41, 2649-045 Cascais', 'Ortopedia'),
    ('350859267', 'Pedro', '938261625', 'Praça da Alegria, 41, 2649-045 Cascais', 'Clínica Geral');

INSERT INTO trabalha (nif, nome, dia_da_semana) VALUES 
    ('350859354', 'Clinica Lisboa Central', '0'),
    ('350859354', 'Clinica Almada Saúde', '1'),
    ('350859326', 'Clinica Almada Saúde', '1'),
    ('350859267', 'Clinica Almada Saúde', '1');

INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES 
    ('22935155532', '199175621', 'Carlos', '926188302', 'Travessa dos Lírios, 97, 8218-568 Faro', '2007-10-28'),
    ('22935155534', '199175623', 'Margarida', '926188304', 'Travessa dos Lírios, 97, 8218-568 Faro', '2007-10-28');

INSERT INTO consulta (id, ssn, nif, nome, data, hora, codigo_sns) VALUES 
    (1, '22935155532', '350859354', 'Clinica Lisboa Central', '2023-01-01', '10:30', NULL),
    (2, '22935155532', '350859354', 'Clinica Lisboa Central', '2023-01-08', '10:30', NULL),
    (3, '22935155534', '350859354', 'Clinica Lisboa Central', '2023-01-01', '14:30', NULL),
    (4, '22935155534', '350859354', 'Clinica Lisboa Central', '2023-01-15', '14:30', NULL),
    (5, '22935155534', '350859354', 'Clinica Almada Saúde', '2023-01-09', '10:30', NULL),
    (6, '22935155532', '350859326', 'Clinica Almada Saúde', '2023-01-09', '11:00', NULL),
    (7, '22935155532', '350859267', 'Clinica Almada Saúde', '2023-01-16', '12:00', NULL);

INSERT INTO observacao (id, parametro, valor) VALUES 
	(1, 'Padrão de Fala', NULL),
	(2, 'Padrão de Fala', NULL),
	(3, 'Temperamento', NULL),
	(4, 'Expressão Emocional', NULL),
    (5, 'Temperamento', NULL),
    (6, 'Padrão de Fala', NULL),
    (7, 'Padrão de Fala', NULL);