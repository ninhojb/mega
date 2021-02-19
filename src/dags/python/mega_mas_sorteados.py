import logging
from contextlib import closing
from datetime import date

from database.banco_de_dados import Banco
from database.persistencia.schema_mega import Jogos, Resultado
from database.postgres import Postgres


def statisticas():
    logging.info('[STATISTICAS]')
    today = date.today()
    hoje = today.strftime('%Y-%m-%d')
    db_mega = Banco()
    database = Postgres()

    with closing(db_mega.conexao):
        numeros = []
        bo = BusinessStatistic(db_mega, database)
        
        max_primeiro = bo.buscar_primeiro()
        for linha in max_primeiro:
            numeros.append(linha[0])

        max_segundo = bo.buscar_segundo()
        for linha in max_segundo:
            numeros.append(linha[0])

        # max_terceiro = bo.buscar_terceiro()
        # max_quarto = bo.buscar_quarto()
        # max_quinto = bo.buscar_quinto()
        # max_sexto = bo.buscar_sexto()
        # inserir_result = bo.inserir_result(hoje, max_primeiro,
        #                                    max_segundo,
        #                                    max_terceiro,
        #                                    max_quarto,
        #                                    max_quinto,
        #                                    max_sexto)

    return (hoje
            # max_primeiro,
            # max_segundo, max_terceiro, max_quarto, max_quinto, max_sexto
            )


class BusinessStatistic(object):
    def __init__(self, db_mega, database: Postgres):
        self.db_mega = db_mega.conexao
        self.database = database
        self.session = db_mega.session

    def buscar_primeiro(self):
        logging.info('[BUSCAR_PRIMEIRO]')

        sql = f'''    
                SELECT DISTINCT 
                   {Resultado.primeiro.name}
                   , count({Resultado.primeiro.name}) as Total
                FROM {Resultado.full_table_name()}
                GROUP BY  {Resultado.primeiro.name}
                ORDER BY 2 DESC
                LIMIT 1
                
            '''
        result = self.database.executar_select(self.db_mega, sql)

        return result

    def buscar_segundo(self):
        logging.info('[BUSCAR_SEGUNDO]')

        sql = f'''    
                        SELECT DISTINCT 
                           {Resultado.segundo.name}
                           , count({Resultado.segundo.name}) as Total
                        FROM {Resultado.full_table_name()}
                        GROUP BY  {Resultado.segundo.name}
                        ORDER BY 2 DESC
                        LIMIT 1

                    '''
        result = self.database.executar_select(self.db_mega, sql)

        return result
