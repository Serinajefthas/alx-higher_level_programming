#!/usr/bin/python3
"""Model containing State and Base"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

