'''
BANCO DE DADOS PARA ARMAZENAR OS NUMEROS DA MEGA SENA

QUE FORAM JOGADOS

DATA: 19-01-2021
'''

import logging
from abc import ABC, abstractmethod


class Database(ABC):
    KWARG_CONNECTION_STRING = 'connection_string'
    KWARG_DATABASE_CONFIG = 'database_config'

    def __init__(self, database_name='Database', driver_conn_string: str = None,
                 alchemy_conn_string: str = None,
                 config: dict = None):
        self.database_name = database_name
        self.driver_conn_string = driver_conn_string
        self.alchemy_conn_string = alchemy_conn_string
        self.config = config or {}
        self._engine = None
        self._conn = None
        self._session = None


import sqlite3


class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect('DB_MEGA.db')
        self.jogos()

    def jogos(self):
        cursor = self.conexao.cursor()

        cursor.execute('''
                CREATE TABLE if not exists jogos(
                    cod_jogo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    pri_num INTEGER,
                    seg_num INTEGER,
                    ter_num INTEGER,
                    qua_num INTEGER,
                    qui_num INTEGER,
                    sex_num INTEGER,
                    dt_carga VARCHAR(10)
                    )
        ''')

        self.conexao.commit()
        cursor.close()
