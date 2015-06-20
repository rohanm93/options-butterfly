from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_options_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

class Options(DeclarativeBase):
	__tablename__ = "options"
	id = Column(Integer, primary_key=True)
	dateTimeUpdated = Column('dateTimeUpdated', DateTime, nullable=True)
	stockName = Column('stockName', String, nullable=True)
	currentPrice = Column('currentPrice', String, nullable=True)
	strikePrice = Column('strikePrice', String, nullable=True)
	askPrice = Column('askPrice', String, nullable=True)
	askQty = Column('askQty', String, nullable=True)
	oi = Column('oi', String, nullable=True)
	# 'c' = call, 'p' = put
	cp = Column('callPut', String, nullable=True)