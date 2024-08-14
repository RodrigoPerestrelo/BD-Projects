INSERT INTO clinica (nome, telefone, morada) VALUES
	('Clinica Lisboa Central', '213456789', 'Rua da Saúde, 123, 1000-001 Lisboa');

INSERT INTO medico (nif, nome, telefone, morada, especialidade) VALUES 
	('350859353', 'Rui Pereirinha', '935810679', 'Praça da Alegria, 41, 2649-045 Cascais', 'Clinica Geral');

INSERT INTO trabalha (nif, nome, dia_da_semana) VALUES 
	('350859353', 'Clinica Lisboa Central', '0');

INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES 
	('22935155532', '199175629', 'António Machado', '926188301', 'Travessa dos Lírios, 97, 8218-568 Faro', '2008-10-28'),
    ('12935155532', '199175628', 'Antónieto', '926188301', 'Travessa dos Lírios, 97, 8218-568 Faro', '2007-10-28');

INSERT INTO consulta (id, ssn, nif, nome, data, hora, codigo_sns) VALUES 
	(1, '22935155532', '350859353', 'Clinica Lisboa Central', '2024-05-27', '16:30', '117850105575'),
    (2, '12935155532', '350859353', 'Clinica Lisboa Central', '2024-05-27', '17:30', '117850105576');

INSERT INTO receita (codigo_sns, medicamento, quantidade) VALUES 
	('117850105575', 'Buspirona', 2),
    ('117850105576', 'Ben-U-Ron', 3),
    ('117850105575', 'Ben-U-Ron', 1);

INSERT INTO observacao (id, parametro, valor) VALUES 
	(1, 'Padrão de Fala', NULL),
    (2, 'Padrão de Fala', NULL);