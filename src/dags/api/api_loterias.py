import requests
import logging

from api import API_Loteria

class ConexaoLoteria:
    def __init__(self, config=None):
        conexao = API_Loteria(config=config)
        self.url = conexao.resultado_conexao()


    def mega_resultado(self):
        r = requests.get(self.url)
        logging.info(r.text)
        return r.text

