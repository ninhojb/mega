# Cria as tabelas


import logging

from database import ConexaoPostgres


class Banco:

    def __init__(self):
        conn = ConexaoPostgres()
        self.conexao = conn.conxexao_postgres()
        self.cria_tabela_jogos()

    def cria_tabela_jogos(self):
        tabela = 'jogos'
        logging.info(f'Criando tabela {tabela}')

        self.conexao.execute('''
                       CREATE TABLE if not exists mega.jogos(
                       cod_jogo SERIAL NOT NULL PRIMARY KEY ,
                       pri_num INT,
                       seg_num INT,
                       ter_num INT,
                       qua_num INT,
                       qui_num INT,
                       sex_num INT,
                       dt_carga DATE)''')

        return f'tabela criado com sucesso {tabela}'
