#!usr/bin/env python
#coding:utf-8
"""
法律法规模型
"""
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,String,Integer,Text,Column

basedir = os.path.dirname(__file__)
filepath = os.path.join(basedir,'law.db')
engine = create_engine('sqlite:///%s'%(filepath))
Base = declarative_base()
class Law(Base):
    __tablename__='law'

    id = Column(String(48),primary_key=True)
    url = Column(Text)
    title = Column(String(48))
    wenhao = Column(String(48))
    publish_date = Column(String(48))
    done_date = Column(String(48))
    publish_department = Column(String(48))
    law_class = Column(String(48))
    zhengwen = Column(Text)

DBSession = sessionmaker(bind=engine)
session = DBSession()

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    pass
    drop_db()
    init_db()

