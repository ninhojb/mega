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
