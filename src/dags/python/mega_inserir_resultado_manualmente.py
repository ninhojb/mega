import logging
from contextlib import closing
from datetime import date

from database.banco_de_dados import Banco
from database.persistencia.schema_mega import Resultado
from database.postgres import Postgres


def inserir_resultado_manualmente():
    today = date.today()
    hoje = today.strftime('%Y-%m-%d')
    logging.info('[RESULTADO_MEGA] ')
    db_mega = Banco()
    database = Postgres()

    with closing(db_mega.conexao):
        bo = BusinessInserir(db_mega, database)

        inserir = bo.inserir_dados(hoje)

    return inserir


class BusinessInserir(object):

    def __init__(self, db_mega, database: Postgres):
        self.db_mega = db_mega.conexao
        self.database = database

    def inserir_dados(self, hoje):
        num_concurso, primeiro, segundo, terceiro, quarto, quinto, sexto, data_sorteio = ['2347', '08', '09', '17',
                                                                                          '30', '58', '60',
                                                                                          '2021-02-20']

        sql = f'''
            INSERT INTO {Resultado.full_table_name()}
                        ({Resultado.num_concurso.name},
                        {Resultado.primeiro.name},
                        {Resultado.segundo.name},
                        {Resultado.terceiro.name},
                        {Resultado.quarto.name},
                        {Resultado.quinto.name},
                        {Resultado.sexto.name},
                        {Resultado.data_solteio.name},
                        {Resultado.dt_carga.name}
                        )
                    VALUES ({num_concurso},{primeiro}, {segundo}, {terceiro}, {quarto}, {quinto}, {sexto},'{data_sorteio}','{hoje}')
            '''
        insert = self.database.executar_insert(self.db_mega, sql)
        return 'INSERIDO'
