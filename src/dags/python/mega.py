import logging

from database.unico import Airflow

banco = Airflow()

def gerar():
    logging.info('enviando a tabela mega')
    tabela = 'mega'
    banco.cria_tabela()
    logging.info("fim ")
    return "deu certo"