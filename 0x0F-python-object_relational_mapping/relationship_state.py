#!/usr/bin/python3
"""
A python file that contains the class definition of a State and an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

class State(Base):
    """A class that links to the MySQL table states"""
    
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
