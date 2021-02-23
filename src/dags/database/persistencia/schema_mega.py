from datetime import datetime

from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

AlchemyEntity = declarative_base()


class Jogos(AlchemyEntity):
    __tablename__ = 'jogos'
    __table_args__ = {"schema": "mega"}

    cod_jogo = Column(Integer, primary_key=True, autoincrement=True)
    pri_num = Column(Integer)
    seg_num = Column(Integer)
    ter_num = Column(Integer)
    qua_num = Column(Integer)
    qui_num = Column(Integer)
    sex_num = Column(Integer)
    dt_carga = Column(TIMESTAMP, default=datetime.now)

    @classmethod
    def full_table_name(cls):
        return f"{cls.__table_args__['schema']}.{cls.__tablename__}"


class Resultado(AlchemyEntity):
    __tablename__ = 'resultados'
    __table_args__ = {"schema": "mega"}

    cod_result = Column(Integer, primary_key=True, autoincrement=True)
    num_concurso = Column(Integer)
    primeiro = Column(Integer)
    segundo = Column(Integer)
    terceiro = Column(Integer)
    quarto = Column(Integer)
    quinto = Column(Integer)
    sexto = Column(Integer)
    data_solteio = Column(TIMESTAMP)
    dt_carga = Column(TIMESTAMP, default=datetime.now)

    @classmethod
    def full_table_name(cls):
        return f"{cls.__table_args__['schema']}.{cls.__tablename__}"


class MasSorteados(AlchemyEntity):
    __tablename__ = 'mas_sorteados'
    __table_args__ = {"schema": "mega"}

    cod_sort = Column(Integer, primary_key=True, autoincrement=True)
    primeiro = Column(Integer)
    segundo = Column(Integer)
    terceiro = Column(Integer)
    quarto = Column(Integer)
    quinto = Column(Integer)
    sexto = Column(Integer)
    dt_carga = Column(TIMESTAMP, default=datetime.now)

    @classmethod
    def full_table_name(cls):
        return f"{cls.__table_args__['schema']}.{cls.__tablename__}"


class MaisJogados(AlchemyEntity):
    __tablename__ = 'mais_jogados'
    __table_args__ = {"schema": "mega"}

    cod_jog = Column(Integer, primary_key=True, autoincrement=True)
    primeiro = Column(Integer)
    segundo = Column(Integer)
    terceiro = Column(Integer)
    quarto = Column(Integer)
    quinto = Column(Integer)
    sexto = Column(Integer)
    dt_carga = Column(TIMESTAMP, default=datetime.now)

    @classmethod
    def full_table_name(cls):
        return f"{cls.__table_args__['schema']}.{cls.__tablename__}"
