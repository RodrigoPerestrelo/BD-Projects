CREATE TABLE horarios (
    id SERIAL PRIMARY KEY,
    data DATE,
    horario TIME
);

DO $$
DECLARE
    dt DATE := CURRENT_DATE;
    hr TIME;
BEGIN
    WHILE dt <= '2024-12-31' LOOP
        -- Inserir horários das 09:00 até 12:30 com intervalos de 30 minutos
        hr := '09:00:00';
        WHILE hr <= '12:30:00' LOOP
            INSERT INTO horarios (data, horario) VALUES (dt, hr);
            hr := hr + INTERVAL '30 minutes';
        END LOOP;

        -- Inserir horários das 14:00 até 18:30 com intervalos de 30 minutos
        hr := '14:00:00';
        WHILE hr <= '18:30:00' LOOP
            INSERT INTO horarios (data, horario) VALUES (dt, hr);
            hr := hr + INTERVAL '30 minutes';
        END LOOP;

        -- Avançar para o próximo dia
        dt := dt + INTERVAL '1 day';
    END LOOP;
END $$;
