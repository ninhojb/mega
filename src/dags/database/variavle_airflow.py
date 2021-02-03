import os
from abc import ABC

from airflow.models import Variable


class Constantes(ABC):
    BLANK = ''

    @staticmethod
    def get_from_environment(nome_var):
        return os.getenv(nome_var)

    @staticmethod
    def get_from_airflow(nome_var):
        return Variable.get(nome_var)


class AirflowVariable:
    POSTGRES_HOST = 'POSTGRES_HOST'
    POSTGRES_PORT = 'POSTGRES_PORT'
    POSTGRES_USER = 'POSTGRES_USER'
    POSTGRES_PASSWD = 'POSTGRES_PASSWD'
    POSTGRES_DATABASE = 'POSTGRES_DATABASE'
