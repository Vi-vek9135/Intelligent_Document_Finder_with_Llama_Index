from sqlalchemy import String, Integer, Column, Boolean, DateTime

from database import Base

import datetime



# For Testing Purpose
# def create_tables(engine):
#     Base.metadata.create_all(engine)



# User Model
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)


# Token Model
class TokenTable(Base):
    __tablename__ = "token"
    user_id = Column(Integer)
    access_toke = Column(String(450), primary_key=True)
    refresh_toke = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.now)
