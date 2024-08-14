-- OUTPUT: Benuron pois o mesmo paciente toma Benurom durante 12 meses seguidos.

INSERT INTO clinica (nome, telefone, morada) VALUES
	('Clinica Lisboa Central', '213456789', 'Rua da Saúde, 123, 1000-001 Lisboa');

INSERT INTO medico (nif, nome, telefone, morada, especialidade) VALUES 
    ('350859354', 'António', '935810678', 'Praça da Alegria, 41, 2649-045 Cascais', 'Cardiologia');

INSERT INTO trabalha (nif, nome, dia_da_semana) VALUES 
    ('350859354', 'Clinica Lisboa Central', '0'),
	('350859354', 'Clinica Lisboa Central', '1'),
	('350859354', 'Clinica Lisboa Central', '2'),
	('350859354', 'Clinica Lisboa Central', '3'),
	('350859354', 'Clinica Lisboa Central', '4'),
	('350859354', 'Clinica Lisboa Central', '5'),
	('350859354', 'Clinica Lisboa Central', '7'),
	('350859354', 'Clinica Lisboa Central', '6');

INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES 
    ('22935155534', '199175623', 'Margarida', '926188304', 'Travessa dos Lírios, 97, 8218-568 Faro', '2007-10-28');

INSERT INTO consulta (ssn, nif, nome, data, hora, codigo_sns) VALUES 
	('22935155534', '350859354', 'Clinica Lisboa Central', '2023-01-01', '9:30', '991636370401'),
    ('22935155534', '350859354', 'Clinica Lisboa Central', '2023-02-01', '10:30', '991636370402'),
    ('22935155534', '350859354', 'Clinica Lisboa Central', '2023-03-01', '11:30', '991636370403'),
    ('22935155534', '350859354', 'Clinica Lisboa Central', '2023-04-01', '14:30', '991636370404'),
    ('22935155534', '350859354', 'Clinica Lisboa Central', '2023-05-01', '15:30', '991636370405'),
	('22935155534', '350859354', 'Clinica Lisboa Central', '2023-06-01', '9:30', '991636370406'),
    ('22935155534', '350859354', 'Clinica Lisboa Central', '2023-07-01', '10:30', '991636370407'),
    ('22935155534', '350859354', 'Clinica Lisboa Central', '2023-08-01', '11:30', '991636370408'),
    ('22935155534', '350859354', 'Clinica Lisboa Central', '2023-09-01', '14:30', '991636370409'),
    ('22935155534', '350859354', 'Clinica Lisboa Central', '2023-10-01', '15:30', '991636370410'),
	('22935155534', '350859354', 'Clinica Lisboa Central', '2023-10-05', '15:30', '991636373410'),
	('22935155534', '350859354', 'Clinica Lisboa Central', '2023-11-01', '9:30', '991636370411'),
    ('22935155534', '350859354', 'Clinica Lisboa Central', '2023-12-01', '10:30', '991636370412');

INSERT INTO receita (codigo_sns, medicamento, quantidade) VALUES 
	('991636370401', 'Benuron', 2),
	('991636370402', 'Benuron', 1),
	('991636370403', 'Benuron', 2),
	('991636370404', 'Benuron', 3),
	('991636370405', 'Benuron', 2),
	('991636370406', 'Benuron', 1),
	('991636370407', 'Benuron', 1),
	('991636370408', 'Benuron', 1),
	('991636370409', 'Benuron', 1),
	('991636370410', 'Benuron', 2),
	('991636373410', 'Benuron', 4),
	('991636370411', 'Benuron', 2),
	('991636370412', 'Benuron', 3);