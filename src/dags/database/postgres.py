# onde coloco as pequisas


import logging

from sqlalchemy_utils.types.pg_composite import psycopg2


class Postgres:

    def __init__(self):
        pass

    def executar_insert(self, conexao, sql):
        logging.info('[EXECUTAR_INSERT] inserir dados na tabelas jogos')
        _conn = conexao
        try:
            resul = _conn.execute(sql)

            return resul

        except (Exception, psycopg2.DatabaseError) as error:
            return logging.info(error)

    def executar_select(self, conexao, sql):
        logging.info('[EXECUTAR_SELECT] Select todos os jogos')
        _conn = conexao
        try:
            resul = _conn.execute(sql)

            return resul

        except (Exception, psycopg2.DatabaseError) as error:
            return logging.info(error)
