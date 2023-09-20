#!/usr/bin/python3
""" Review module for the HBNB project """
import models
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """ Review classto store review information """
    if models.mode == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
