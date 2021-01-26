-- entra no container
docker exec -it dev_postgres_1 bash

-- connecta via terminal
psql -U airflow


-- COMMANDOS SQLs
--create USER aldata with PASSWORD 'Prudencia@2019' CREATEDB;
create user aldata with PASSWORD 'Foco@2020';

create DATABASE voz_dw
    with OWNER aldata;

grant ALL PRIVILEGES  on database voz_dw to aldata;

exit

-- CRIA SCHEMAS
-- use voz_dw
--CREATE SCHEMA IF NOT EXISTS meta AUTHORIZATION aldata;
--CREATE SCHEMA IF NOT EXISTS raw AUTHORIZATION aldata;
--CREATE SCHEMA IF NOT EXISTS cm AUTHORIZATION aldata;
--CREATE SCHEMA IF NOT EXISTS crm AUTHORIZATION aldata;
