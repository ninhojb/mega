import logging
from contextlib import closing
from datetime import date

from database.banco_de_dados import Banco
from database.persistencia.schema_mega import Jogos
from database.postgres import Postgres


def mostrar_jogos_atuais():
    today = date.today()
    hoje = today.strftime('%Y-%m-%d')
    db_mega = Banco()
    database = Postgres()

    with closing(db_mega.conexao):
        bo = BusinessMostrarJogosAtuais(db_mega, database)
        criar_sql = bo.criar_sql(hoje)
        executar_sql = bo.executar_sql(criar_sql)

        for lista in executar_sql:
            logging.info(lista)

    return '[MOSTRAR_JOGOS_ATUAIS] Sucesso !!!'


class BusinessMostrarJogosAtuais(object):
    def __init__(self, db_mega, database: Postgres):
        self.db_mega = db_mega.conexao
        self.database = database

    def criar_sql(self, hoje):
        logging.info('[CRIAR_SQL] Gerando SQL')
        _sql = f"""
                SELECT *
                FROM {Jogos.full_table_name()}
                WHERE dt_carga = '{hoje}'
                """

        logging.info(_sql)
        return _sql

    def executar_sql(self, criar_sql):
        logging.info('[EXECUTAR_SQL] Executando SQL')
        resul = self.database.executar_select(self.db_mega, criar_sql)

        return resul