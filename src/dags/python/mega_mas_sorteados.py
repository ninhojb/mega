import logging
from contextlib import closing
from datetime import date

from sqlalchemy import func

from database.banco_de_dados import Banco
from database.persistencia.schema_mega import Jogos, Resultado, MasSorteados
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

        max_terceiro = bo.buscar_terceiro()
        for linha in max_terceiro:
            numeros.append(linha[0])

        max_quarto = bo.buscar_quarto()
        for linha in max_quarto:
            numeros.append(linha[0])

        max_quinto = bo.buscar_quinto()
        for linha in max_quinto:
            numeros.append(linha[0])

        max_sexto = bo.buscar_sexto()
        for linha in max_sexto:
            numeros.append(linha[0])

        verificar = bo.verificar_insert()
        if str(hoje) != str(verificar):
            inserir_result = bo.inserir_result(hoje, numeros)
        else:
            logging.info('Dados jah foi inserido')

    return (f'{hoje}, {numeros}')


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

    def buscar_terceiro(self):
        logging.info('[BUSCAR_TERCEIRO]')

        sql = f'''    
                SELECT DISTINCT 
                   {Resultado.terceiro.name}
                   , count({Resultado.terceiro.name}) as Total
                FROM {Resultado.full_table_name()}
                GROUP BY  {Resultado.terceiro.name}
                ORDER BY 2 DESC
                LIMIT 1

                '''
        result = self.database.executar_select(self.db_mega, sql)

        return result

    def buscar_quarto(self):
        logging.info('[BUSCAR_QUARTO]')

        sql = f'''    
                SELECT DISTINCT 
                   {Resultado.quarto.name}
                   , count({Resultado.quarto.name}) as Total
                FROM {Resultado.full_table_name()}
                GROUP BY  {Resultado.quarto.name}
                ORDER BY 2 DESC
                LIMIT 1

                '''
        result = self.database.executar_select(self.db_mega, sql)
        return result

    def buscar_quinto(self):
        logging.info('[BUSCAR_QUINTO]')

        sql = f'''    
                SELECT DISTINCT 
                   {Resultado.quinto.name}
                   , count({Resultado.quinto.name}) as Total
                FROM {Resultado.full_table_name()}
                GROUP BY  {Resultado.quinto.name}
                ORDER BY 2 DESC
                LIMIT 1

            '''
        result = self.database.executar_select(self.db_mega, sql)
        return result

    def buscar_sexto(self):
        logging.info('[BUSCAR_SEXTO]')

        sql = f'''    
                SELECT DISTINCT 
                   {Resultado.sexto.name}
                   , count({Resultado.sexto.name}) as Total
                FROM {Resultado.full_table_name()}
                GROUP BY  {Resultado.sexto.name}
                ORDER BY 2 DESC
                LIMIT 1

            '''
        result = self.database.executar_select(self.db_mega, sql)
        return result

    def verificar_insert(self):
        logging.info('[VERIFICAR_INSERT]')
        resul = self.session.query(MasSorteados)

        for dados in resul:
            logging.info(f'resultado: {dados.dt_carga}')

            return dados.dt_carga
        return 1

    def inserir_result(self, hoje, numeros):
        logging.info('[INSERIR_RESULT]')
        primeiro, segundo, terceiro, quarto, quinto, sexto = numeros

        sql = f'''
                INSERT INTO {MasSorteados.full_table_name()}
                            ({MasSorteados.primeiro.name},
                            {MasSorteados.segundo.name},
                            {MasSorteados.terceiro.name},
                            {MasSorteados.quarto.name},
                            {MasSorteados.quinto.name},
                            {MasSorteados.sexto.name},
                            {MasSorteados.dt_carga.name}
                            )
                VALUES ({primeiro}, {segundo}, {terceiro}, {quarto}, {quinto}, {sexto}, '{hoje}')
            '''

        insert = self.database.executar_insert(self.db_mega, sql)
        return 'INSERIDO'


