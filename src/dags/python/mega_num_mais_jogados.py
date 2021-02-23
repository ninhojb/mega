import logging
from contextlib import closing
from datetime import date

from database.banco_de_dados import Banco
from database.persistencia.schema_mega import Jogos, Resultado, MasSorteados, MaisJogados
from database.postgres import Postgres


def num_mais_jogados():
    logging.info('[NUM_MAIS_JOGADOS]')
    today = date.today()
    hoje = today.strftime('%Y-%m-%d')
    db_mega = Banco()
    database = Postgres()

    with closing(db_mega.conexao):
        numeros = []
        bo = BusinessMaisJogados(db_mega, database)

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


class BusinessMaisJogados(object):
    def __init__(self, db_mega, database: Postgres):
        self.db_mega = db_mega.conexao
        self.database = database
        self.session = db_mega.session

    def buscar_primeiro(self):
        logging.info('[BUSCAR_PRIMEIRO]')

        sql = f'''    
                SELECT DISTINCT 
                   {Jogos.pri_num.name}
                   , count({Jogos.pri_num.name}) as Total
                FROM {Jogos.full_table_name()}
                GROUP BY  {Jogos.pri_num.name}
                ORDER BY 2 DESC
                LIMIT 1

            '''
        result = self.database.executar_select(self.db_mega, sql)

        return result

    def buscar_segundo(self):
        logging.info('[BUSCAR_SEGUNDO]')

        sql = f'''    
                SELECT DISTINCT 
                   {Jogos.seg_num.name}
                   , count({Jogos.seg_num.name}) as Total
                FROM {Jogos.full_table_name()}
                GROUP BY  {Jogos.seg_num.name}
                ORDER BY 2 DESC
                LIMIT 1

                    '''
        result = self.database.executar_select(self.db_mega, sql)

        return result

    def buscar_terceiro(self):
        logging.info('[BUSCAR_TERCEIRO]')

        sql = f'''    
                SELECT DISTINCT 
                   {Jogos.ter_num.name}
                   , count({Jogos.ter_num.name}) as Total
                FROM {Jogos.full_table_name()}
                GROUP BY  {Jogos.ter_num.name}
                ORDER BY 2 DESC
                LIMIT 1

                '''
        result = self.database.executar_select(self.db_mega, sql)

        return result

    def buscar_quarto(self):
        logging.info('[BUSCAR_QUARTO]')

        sql = f'''    
                SELECT DISTINCT 
                   {Jogos.qua_num.name}
                   , count({Jogos.qua_num.name}) as Total
                FROM {Jogos.full_table_name()}
                GROUP BY  {Jogos.qua_num.name}
                ORDER BY 2 DESC
                LIMIT 1

                '''
        result = self.database.executar_select(self.db_mega, sql)
        return result

    def buscar_quinto(self):
        logging.info('[BUSCAR_QUINTO]')

        sql = f'''    
                SELECT DISTINCT 
                   {Jogos.qui_num.name}
                   , count({Jogos.qui_num.name}) as Total
                FROM {Jogos.full_table_name()}
                GROUP BY  {Jogos.qui_num.name}
                ORDER BY 2 DESC
                LIMIT 1

            '''
        result = self.database.executar_select(self.db_mega, sql)
        return result

    def buscar_sexto(self):
        logging.info('[BUSCAR_SEXTO]')

        sql = f'''    
                SELECT DISTINCT 
                   {Jogos.sex_num.name}
                   , count({Jogos.sex_num.name}) as Total
                FROM {Jogos.full_table_name()}
                GROUP BY  {Jogos.sex_num.name}
                ORDER BY 2 DESC
                LIMIT 1

            '''
        result = self.database.executar_select(self.db_mega, sql)
        return result

    def verificar_insert(self):
        logging.info('[VERIFICAR_INSERT]')
        resul = self.session.query(MaisJogados)

        for dados in resul:
            logging.info(f'resultado: {dados.dt_carga}')

            return dados.dt_carga
        return 1

    def inserir_result(self, hoje, numeros):
        logging.info('[INSERIR_RESULT]')
        primeiro, segundo, terceiro, quarto, quinto, sexto = numeros

        sql = f'''
                INSERT INTO {MaisJogados.full_table_name()}
                            ({MaisJogados.primeiro.name},
                            {MaisJogados.segundo.name},
                            {MaisJogados.terceiro.name},
                            {MaisJogados.quarto.name},
                            {MaisJogados.quinto.name},
                            {MaisJogados.sexto.name},
                            {MaisJogados.dt_carga.name}
                            )
                VALUES ({primeiro}, {segundo}, {terceiro}, {quarto}, {quinto}, {sexto}, '{hoje}')
            '''

        insert = self.database.executar_insert(self.db_mega, sql)
        return 'INSERIDO'
