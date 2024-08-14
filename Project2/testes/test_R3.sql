INSERT INTO clinica (nome, telefone, morada) VALUES
	('Clinica Lisboa Central', '213456789', 'Rua da Saúde, 123, 1000-001 Lisboa');

INSERT INTO medico (nif, nome, telefone, morada, especialidade) VALUES 
	('350859353', 'Rui Pereirinha', '935810679', 'Praça da Alegria, 41, 2649-045 Cascais', 'Clinica Geral');

INSERT INTO trabalha (nif, nome, dia_da_semana) VALUES 
	('350859353', 'Clinica Lisboa Central', '0');

INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES 
	('22935155532', '199175629', 'António Machado', '926188301', 'Travessa dos Lírios, 97, 8218-568 Faro', '2007-10-28');

INSERT INTO consulta (id, ssn, nif, nome, data, hora, codigo_sns) VALUES 
	(1, '22935155532', '350859353', 'Clinica Lisboa Central', '2023-01-02', '19:30', '117850105575');