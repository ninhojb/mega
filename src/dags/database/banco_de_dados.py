from database import Database

from database.postgres import PostgresDB, POSTGRES_PSYCOPG2_URI, POSTGRES_PSYCOPG2_ALCHEMY_URI


class AbstractVozDatabase(Database):

    def connect_new(self, **kwargs):
        raise NotImplemented

    def sequence_nextval(self, sequence):
        raise NotImplemented

    def execute_fetchmany(self, sql, parameters=None, size=100, subset=True, **kwargs):
        raise NotImplemented

    def inserir_dataframe(self, dataframe, tabela, **kwargs):
        # return self.persist_dataframe_2_db(dataframe, tabela, **kwargs)
        pass


class AbstractVozPostgres(Database, AbstractVozDatabase):
    pass


class Airflow(AbstractVozPostgres):

    def __init__(self, config=None, **kwargs):
        if not config:
            config = kwargs.get(self.KWARG_DATABASE_CONFIG)
            if not config:
                config = {"host": 'localhost',
                          "port": 5433,
                          "database": 'airflow',
                          "user": 'airflow',
                          "password": 'airflow'}

        str_driver = POSTGRES_PSYCOPG2_URI.format(**config)
        str_alchemy = POSTGRES_PSYCOPG2_ALCHEMY_URI.format(**config)
        super().__init__('airflow', str_driver, str_alchemy, config)

class Postgres(AbstractVozPostgres):

    def __init__(self, config=None, **kwargs):
        if not config:
            config = kwargs.get(self.KWARG_DATABASE_CONFIG)
            if not config:
                config = {"host": 'localhost',
                          "port": 5433,
                          "database": 'mega',
                          "user": 'mega',
                          "password": 'Mega2021'}

        str_driver = POSTGRES_PSYCOPG2_URI.format(**config)
        str_alchemy = POSTGRES_PSYCOPG2_ALCHEMY_URI.format(**config)
        super().__init__('airflow', str_driver, str_alchemy, config)