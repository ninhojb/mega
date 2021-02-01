import logging

from sqlalchemy import create_engine

class Airflow:

    def __init__(self):
        POSTGRES_PSYCOPG2_ALCHEMY_URI = 'postgres+psycopg2://{user}:{password}@{host}:{port}/{database}'
        config = {"host": 'postgres',
                  "port": int(5432),
                  "database": 'airflow',
                  "user": 'airflow',
                  "password": 'airflow'}

        config1 = POSTGRES_PSYCOPG2_ALCHEMY_URI.format(**config)

        self.str_alchemy = config1

    def cria_tabela(self):
        tabela = 'mega'
        logging.info(f'Criando tabela {tabela}')

        engine = create_engine(self.str_alchemy)
        conn = engine.connect()
        conn.execute('''
                    CREATE TABLE if not exists mega.jogos(
                    cod_jogo SERIAL NOT NULL PRIMARY KEY ,
                    pri_num INT,
                    seg_num INT,
                    ter_num INT,
                    qua_num INT,
                    qui_num INT,
                    sex_num INT,
                    dt_carga DATE)''')

        # --conn.commit()
        conn.close()

        return f'tabela criado com sucesso {tabela}'
