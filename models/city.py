#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if models.mode == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(
                String(60), ForeignKey(
                    'states.id', ondelete='CASCADE'), nullable=False)
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """City object initialization"""
        super().__init__(*args, **kwargs)
