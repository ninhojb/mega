# Conexao com o Database

from sqlalchemy import create_engine

from database.variaveis_airflow import AirflowVariable, Constantes


class ConexaoPostgres:
    def __init__(self):
        POSTGRES_PSYCOPG2_ALCHEMY_URI = 'postgres+psycopg2://{user}:{password}@{host}:{port}/{database}'

        config = {"host": Constantes.get_from_airflow(AirflowVariable.POSTGRES_HOST),
                  "port": int(Constantes.get_from_airflow(AirflowVariable.POSTGRES_PORT)),
                  "database": Constantes.get_from_airflow(AirflowVariable.POSTGRES_DATABASE),
                  "user": Constantes.get_from_airflow(AirflowVariable.POSTGRES_USER),
                  "password": Constantes.get_from_airflow(AirflowVariable.POSTGRES_PASSWD)}

        str_alchemy = POSTGRES_PSYCOPG2_ALCHEMY_URI.format(**config)

        self.conn = str_alchemy

    def conxexao_postgres(self):
        engine = create_engine(self.conn)
        _conn = engine.connect()
        return _conn
