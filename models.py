from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer,autoincrement=True, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    home = Column(String)
    street = Column(String)  
    latitude = Column(String)  
    longitude = Column(String)  