#!/usr/bin/python3
"""Test for BaseModel """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
from os import getenv


class test_basemodel(unittest.TestCase):
    """This tests for class BaseModel """

    def __init__(self, *args, **kwargs):
        """Tests is the type is BaseModel"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """This sets up the test """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """This checks for default value """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """This tests if the method behaves as expected """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Returns the expected results called with int keyword args """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str_representation(self):
        """Test the __str__ representation of BaseModel"""
        expected_str = "[BaseModel] ({}) {}".format(self.basemodel.id,
                        self.basemodel.__dict__)
        self.assertEqual(str(self.basemodel), expected_str)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Tests the string lenght of a method """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                        i.__dict__))

    def test_todict(self):
        """Tests if dictionary conversion works """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Tests for any behavior when no kwargs are passed """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """This tests for any behavior with a single kwargs """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """This checks for id method """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """This tests if created_at works """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """This tests for updates """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_default_constructor(self):
        """Test the default constructor of BaseModel"""
        self.assertIsInstance(self.basemodel, BaseModel)
        self.assertIsInstance(self.basemodel.id, str)
        self.assertIsInstance(self.basemodel.created_at, datetime.datetime)
        self.assertIsInstance(self.basemodel.updated_at, datetime.datetime)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        self.basemodel.name = "Test"
        self.basemodel.age = 25
        self.basemodel.save()
        base_dict = self.basemodel.to_dict()
        expected_keys = ["id", "created_at", "updated_at", "name", "age",
                        "__class__"]
        self.assertEqual(sorted(base_dict.keys()), sorted(expected_keys))
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(base_dict['name'], "Test")
        self.assertEqual(base_dict['age'], 25)

     def test_init_BaseModel(self):
        """Tests if base is type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_from_dict(self):
        """Test creating a BaseModel instance from a dictionary"""
        data = {
                "id": "123",
                "created_at": "2023-01-01T00:00:00",
                "updated_at": "2023-01-02T00:00:00",
                "name": "Test",
                "__class__": "BaseModel"
        }
        new_instance = BaseModel(**data)
        self.assertEqual(new_instance.id, "123")
        self.assertEqual(new_instance.created_at,
                        datetime.datetime(2023, 1, 1, 0, 0))
        self.assertEqual(new_instance.updated_at,
                        datetime.datetime(2023, 1, 2, 0, 0))
        self.assertEqual(new_instance.name, "Test")
        self.assertIsInstance(new_instance, BaseModel)


if __name__ == "__main__":
    unittest.main()
