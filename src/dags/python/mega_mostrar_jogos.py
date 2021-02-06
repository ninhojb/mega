import logging
from contextlib import closing

from database.banco_de_dados import Banco
from database.persistencia.schema_mega import Jogos
from database.postgres import Postgres


def mostrar_jogos_gerados():
    db_mega = Banco()
    database = Postgres()
    with closing(db_mega.conexao):
        bo = BusinessMostrarJogos(db_mega, database)
        sql = bo.gerar_sql()
        executar_sql_sql = bo.executar_sql(sql)

        for lista in executar_sql_sql:
            logging.info(lista)

    return '[MOSTRAR_JOGOS_GERADOS] Sucesso'


class BusinessMostrarJogos(object):
    def __init__(self, db_mega, database: Postgres):
        self.db_mega = db_mega.conexao
        self.database = database

    def gerar_sql(self):
        logging.info('[GERAR_SQL] Gerando sql')
        sql = f"""
            SELECT *
            FROM {Jogos.full_table_name()}
        """
        return sql

    def executar_sql(self, sql):
        logging.info('[EXECUTAR_SQL] Executando sql')
        resul = self.database.executar_select(self.db_mega, sql)
        return resul
