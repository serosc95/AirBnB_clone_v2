#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    addresses = relationship("City", backref="", cascade="all, delete")
