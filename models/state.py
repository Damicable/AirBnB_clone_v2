#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if models.mode == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ""

    if models.mode != 'db':
        @property
        def cities(self):
            """Getter method to fetch cities in a state"""
            c_l = []
            city_objs = models.storage.all(City)
            for val in list(city_objs.values()):
                if val.state_id == self.id:
                    c_l.append(val)
            return c_l
