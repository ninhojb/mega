# onde coloco as pequisas


import logging

from sqlalchemy_utils.types.pg_composite import psycopg2

from database.banco_de_dados import Banco


class Postgres:

    def __init__(self, cod_jogo='', pri_num='', seg_num='',
                 ter_num='', qua_num='', qui_num='', sex_num='', dt_carga=''):
        self.info = []
        self.cod_jogo = cod_jogo
        self.pri_num = pri_num
        self.seg_num = seg_num
        self.ter_num = ter_num
        self.qua_num = qua_num
        self.qui_num = qui_num
        self.sex_num = sex_num
        self.dt_carga = dt_carga
        self.banco = Banco()

    def inserir_jogos(self):
        logging.info('inserir dados na tabelas jogos')

        try:
            cursor = self.banco.conexao
            cursor.execute(f'''
                INSERT INTO mega.jogos(
                    pri_num,
                    seg_num,
                    ter_num,
                    qua_num,
                    qui_num,
                    sex_num,
                    dt_carga
                )
                VALUES ({self.pri_num},{self.seg_num},{self.ter_num},{self.qua_num},{self.qui_num},{self.sex_num},'{self.dt_carga}')''')

            return logging.info('Cadastro realizado com sucesso')
        except (Exception, psycopg2.DatabaseError) as error:
            return logging.info(error)
