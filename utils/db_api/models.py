# from asyncore import file_dispatcher
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger, Text, Boolean, Date

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, Session

from datetime import datetime, date

DATABASE_NAME = 'db.sqlite3'

Base = declarative_base()

engine = create_engine(f"sqlite:///{DATABASE_NAME}")
session = Session(bind=engine)

documents_tags = Table('association', Base.metadata,
                       Column('key_word', ForeignKey('tags.id')),
                       Column('file_name', ForeignKey('files.id'))
                       )


class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer(), primary_key=True)
    key_word = Column(String)


class Documents(Base):
    __tablename__ = 'files'
    id = Column(Integer(), primary_key=True)
    file_name = Column(String)
    file_path = Column(String)
    tags = relationship("Tags", secondary=documents_tags, backref="file")




def create_db():
    Base.metadata.create_all(engine)

