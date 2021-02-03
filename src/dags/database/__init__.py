# Conexao com o Database

from sqlalchemy import create_engine


class ConexaoPostgres:
    def __init__(self):
        POSTGRES_PSYCOPG2_ALCHEMY_URI = 'postgres+psycopg2://{user}:{password}@{host}:{port}/{database}'
        config = {"host": 'postgres',
                  "port": int(5432),
                  "database": 'airflow',
                  "user": 'airflow',
                  "password": 'airflow'}

        conn = POSTGRES_PSYCOPG2_ALCHEMY_URI.format(**config)

        self.str_alchemy = conn

    def conxexao_postgres(self):
        engine = create_engine(self.str_alchemy)
        conn = engine.connect()
        return conn
