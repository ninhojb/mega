import logging
from contextlib import closing
from datetime import date

from database.banco_de_dados import Banco
from database.persistencia.schema_mega import Jogos
from database.postgres import Postgres
from database import ConexaoPostgres


def mostrar_jogos_atuais():
    today = date.today()
    hoje = today.strftime('%Y-%m-%d')
    db_mega = Banco()
    database = Postgres()

    with closing(db_mega.conexao):
        bo = BusinessMostrarJogosAtuais(db_mega, database)
        criar_sql = bo.criar_sql(hoje)
        executar_sql = bo.executar_sql(criar_sql)
        select_session = bo.select_session(hoje)

        for lista in select_session:
            logging.info(f'{lista.dt_carga}, {lista.pri_num}, {lista.seg_num}, {lista.ter_num}, '
                         f'{lista.qua_num}, {lista.qui_num}, {lista.sex_num}')

    return '[MOSTRAR_JOGOS_ATUAIS] Sucesso !!!'


class BusinessMostrarJogosAtuais(object):
    def __init__(self, db_mega, database: Postgres):
        self.db_mega = db_mega.conexao
        self.database = database
        self.session = db_mega.session

    def criar_sql(self, hoje):
        logging.info('[CRIAR_SQL] Gerando SQL')
        _sql = f"""
                SELECT *
                FROM {Jogos.full_table_name()}
                WHERE dt_carga = '{hoje}'
                """
        return _sql

    def executar_sql(self, criar_sql):
        logging.info('[EXECUTAR_SQL] Executando SQL')
        resul = self.database.executar_select(self.db_mega, criar_sql)

        return resul

    def select_session(self, hoje):
        logging.info(['SELECT_SESSION('])
        result = self.session.query(Jogos) \
            .filter(Jogos.dt_carga == hoje)

        return result
