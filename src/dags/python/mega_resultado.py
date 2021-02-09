import json
import logging
from contextlib import closing
from datetime import date

from api.api_loterias import ConexaoLoteria
from database.banco_de_dados import Banco
from database.persistencia.schema_mega import Resultado
from database.postgres import Postgres


def resultado_mega():
    today = date.today()
    hoje = today.strftime('%Y-%m-%d')
    logging.info('[RESULTADO_MEGA] ')
    db_mega = Banco()
    database = Postgres()

    with closing(db_mega.conexao):
        bo = BusinessResultados(db_mega, database)
        resultado = bo.pegar_resultado()
        verificar_resultado = bo.verificar_resultado(resultado)
        if verificar_resultado == 1:
            sql = bo.gera_sql(resultado, hoje)
            inserir_resultado = bo.inserir_resultado(sql)

            return "Sucesso com Gravaçao de dados"
        else:
            return "Sucesso sem Gravaçao de dados"


class BusinessResultados(object):

    def __init__(self, db_mega, database: Postgres, **kwargs):
        api = ConexaoLoteria(**kwargs)
        self.api_resul = api.mega_resultado()
        self.db_mega = db_mega.conexao
        self.database = database

    def pegar_resultado(self):
        logging.info('[PEGAR_RESULTAD]')
        resul = self.api_resul
        objeto = json.loads(resul)
        dezenas = objeto['dezenas']
        data_concurso = objeto['data_concurso']
        numero_concurso = objeto['numero_concurso']

        logging.warning(f'{numero_concurso}, {dezenas}, {data_concurso}')
        return data_concurso, dezenas, numero_concurso

    def verificar_resultado(self, resultado):
        logging.info('[VERIFICAR_RESULTADO]')
        data, dezenas, numero_concurso = resultado
        sql = f"""
                SELECT max({Resultado.num_concurso.name})
                FROM {Resultado.full_table_name()}
                WHERE {Resultado.num_concurso.name} = {numero_concurso}
        """
        result = self.database.executar_select(self.db_mega, sql)

        for res in result:
            logging.info(res[0])
            logging.info(numero_concurso)
            if res[0] == numero_concurso:
                logging.warning('Resultado jah esta gravado na tabela')
                return 0
            else:
                return 1

    def gera_sql(self, resultado, hoje):
        logging.info('[GERA_SQL]')
        data, dezenas, numero_concurso = resultado
        self.data_resultado = data.split("T")
        self.data_resultado = self.data_resultado[0]
        self.numero_concurso = numero_concurso

        self.primeiro = dezenas[0]
        self.segundo = dezenas[1]
        self.terceiro = dezenas[2]
        self.quarto = dezenas[3]
        self.quinto = dezenas[4]
        self.sexto = dezenas[5]

        sql = f"""
                INSERT INTO {Resultado.full_table_name()}
                            ({Resultado.num_concurso.name},
                             {Resultado.primeiro.name},
                             {Resultado.segundo.name},
                             {Resultado.terceiro.name},
                             {Resultado.quarto.name},
                             {Resultado.quinto.name},
                             {Resultado.sexto.name},
                             {Resultado.data_solteio.name},
                             {Resultado.dt_carga.name})
                VALUES({self.numero_concurso},{self.primeiro},{self.segundo},{self.terceiro},
                        {self.quarto},{self.quinto},{self.sexto},'{self.data_resultado}', '{hoje}')
            """

        return sql

    def inserir_resultado(self, sql):
        logging.info('[INSERIR_RESULTADO] Inseridno Resultado na tabela')
        resul = self.database.executar_insert(self.db_mega, sql)

        return resul
