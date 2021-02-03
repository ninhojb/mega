import logging
from datetime import date

import numpy as np

from database.postgres import Postgres


def gerar():
    postgres = Postgres()
    today = date.today()
    now = today.strftime('%Y-%m-%d')
    logging.info(f'Gerar numeros na data: {now}')
    total = 0

    numeros = np.random.randint(1, 61, (2, 6))
    numeros = np.sort(numeros)

    for i in numeros:
        postgres.pri_num = int(i[0])
        postgres.seg_num = int(i[1])
        postgres.ter_num = int(i[2])
        postgres.qua_num = int(i[3])
        postgres.qui_num = int(i[4])
        postgres.sex_num = int(i[5])
        postgres.dt_carga = now

        total += 1

        logging.info(postgres.inserir_jogos())

    return f"Inserido com sucesso {total} jogos"
