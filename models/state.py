#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref=backref("State",
                          cascade="all, delete"))

    if os.getenv("HBNB_TYPE_STORAGE" != "db"):
        @property
        def cities(self):
        """List of City instances with state_id equals"""	        
        city_list = []
        all_cities = models.storage.all(City)
        for obj in all_cities.values():
            if obj.state_id == self.id:
                city_list.append(obj)
        return city_list
