#!/usr/bin/python3
"""DB storage level definitiion module"""
from os import getenv
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """The DB vversion of storage for the AirBnB clone"""
    __engine = None
    __session = None

    def __init__(self):
        """Initiate a DB Storage object"""
        HBNB_ENV = getenv('HBNB_ENV')
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB), pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrieve data from DB depending on class if provided"""
        db_dict = {}
        for i in classes:
            if cls is None or cls == i or cls == classes[i]:
                instances = self.__session.query(classes[i]).all()
                for instance in instances:
                    idx = instance.__class__.__name__ + '.' + instance.id
                    db_dict[idx] = instance
        return (db_dict)

    def new(self, obj):
        """Create a new db value"""
        self.__session.add(obj)

    def save(self):
        """Persist created instances to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the database if it exists"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Refresh db data"""
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_maker)
        self.__session = Session

    def close(self):
        """End a db session"""
        self.__session.remove()
