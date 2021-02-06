import logging
from contextlib import closing
from datetime import date

import numpy as np

from database.banco_de_dados import Banco
from database.persistencia.schema_mega import Jogos
from database.postgres import Postgres


def mega_gerar():
    today = date.today()
    hoje = today.strftime('%Y-%m-%d')
    db_mega = Banco()
    database = Postgres()
    with closing(db_mega.conexao):
        bo = BusinessJogos(db_mega, database)
        numeros = bo.gerar_numeros()
        sql = bo.gerar_sql(numeros, hoje)
        inserir_numeros = bo.inserir_jogos(sql)

    return f'[{hoje}] Gerado os numeros {numeros[0]} com Sucesso'


class BusinessJogos(object):

    def __init__(self, db_mega, database: Postgres):
        self.db_mega = db_mega.conexao
        self.database = database

    def gerar_numeros(self):
        logging.info('[INSERIR_JOGOS] Gerando Jogos')

        numeros = np.random.randint(1, 61, (1, 6))
        numeros = np.sort(numeros)

        return numeros

    def gerar_sql(self, numeros, hoje):
        for i in numeros:
            self.pri_num = int(i[0])
            self.seg_num = int(i[1])
            self.ter_num = int(i[2])
            self.qua_num = int(i[3])
            self.qui_num = int(i[4])
            self.sex_num = int(i[5])
        sql = f"""
                INSERT INTO {Jogos.full_table_name()}
                            ({Jogos.pri_num.name},
                             {Jogos.seg_num.name},
                             {Jogos.ter_num.name},
                             {Jogos.qua_num.name},
                             {Jogos.qui_num.name},
                             {Jogos.sex_num.name},
                             {Jogos.dt_carga.name})
                VALUES({self.pri_num},{self.seg_num},{self.ter_num},
                        {self.qua_num},{self.qui_num},{self.sex_num},'{hoje}')
            """
        return sql

    def inserir_jogos(self, sql):
        logging.info('[INSERIR_JOGOS] Inserindo Jogos no DB')
        inserir = self.database.executar_insert(self.db_mega, sql)
        return inserir
