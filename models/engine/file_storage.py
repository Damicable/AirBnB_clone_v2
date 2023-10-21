#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models curriently in storage"""
        if cls and cls.__name__ in classes:
            cls_obj = {}
            for key, val in self.__objects.items():
                cls_val = key.split('.')[0]
                if cls_val == cls.__name__:
                    cls_obj[key] = val
            return cls_obj
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            idx = obj.__class__.__name__ + '.' + obj.id
            self.__objects[idx] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for i, j in self.__objects.items():
            temp[i] = j.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
            for key, val in temp.items():
                self.__objects[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from storage"""
        if obj:
            idx = obj.__class__.__name__ + '.' + obj.id
            if idx in self.__objects.keys():
                del self.__objects[idx]

    def close(self):
        """This trigger reload method to deserialize JSON to objects"""
        self.reload()
