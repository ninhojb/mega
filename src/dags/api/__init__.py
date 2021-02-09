import logging

from database.variaveis_airflow import Constantes, LOTERIAS


class API_Loteria:
    def __init__(self, **kwargs):
        API_LOTERIAS = 'https://apiloterias.com.br/app/resultado?' \
                       'loteria={NOME_DA_LOTERIA}&token={TOKEN}&concurso={NUMERO_DO_CONCURSO}'

        config = kwargs.get('config')
        if not config:
            config = {'TOKEN': str(Constantes.get_from_airflow(LOTERIAS.TOKEN_LOTERIA)),
                      'NOME_DA_LOTERIA': Constantes.get_from_airflow(LOTERIAS.NOME_DA_LOTERIA),
                      'NUMERO_DO_CONCURSO': int(Constantes.get_from_airflow(LOTERIAS.NUMERO_DO_CONCURSO))
                      }
        self.api_mega = API_LOTERIAS.format(**config)

    def resultado_conexao(self):
        return self.api_mega
