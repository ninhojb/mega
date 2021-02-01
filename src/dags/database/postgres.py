# onde coloco as pequisas


import logging
from contextlib import closing

import pandas as pd

from dags.database import Database

DEFAULT_CSV_COLS_DELIM = '\x01'

POSTGRES_PSYCOPG2_ALCHEMY_URI = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
POSTGRES_PSYCOPG2_URI = "host='{host}' port='{port}' dbname='{database}' user='{user}' password='{password}'"


class PostgresDB(Database):

    def prepare_sql_statement(self, sql, **kwargs):
        is_psycopg2_replace = kwargs.get('psycopg2_replace', True)

        atencao = r"[prepare_sql_statement] ATENCAO: psycopg2 utiliza '%s' " \
                  r"AO INVES do comum '?' para queries parametrizadas."
        atencao = f"{atencao} Realizando replace '? -> %s', Ok?[{is_psycopg2_replace}]"
        print(atencao)

        sql = sql.replace('?', '%s') if is_psycopg2_replace else sql
        return sql
