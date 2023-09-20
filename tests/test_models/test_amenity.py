#!/usr/bin/python3
"""Unit tests for Amenity class """
import unittest
import os
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pep8


class test_Amenity(test_basemodel):
    """This test for amenity class"""

    def __init__(self, *args, **kwargs):
        """Initializing the test cases """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.amenity

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Amenity(self):
        """Testing  pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_name_attribute(self):
        """Tests for new string length """
        new_amenity = self.value()
        self.assertEqual(type(new_amenity.name), str)

    def test_checking_for_docstring_Amenity(self):
        """Testing for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """Tests if amenity have attibutes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_str_method(self):
        """Test the __str__ method of Amenity"""
        new_amenity = self.value()
        expected_str = "[{}] ({}) {}".format(self.name, new_amenity.id,
                new_amenity.__dict__)
        self.assertEqual(str(new_amenity), expected_str)

    def test_is_subclass_Amenity(self):
        """Tests if Amenity is subclass of Basemodel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """Tests attribute type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def test_save_Amenity(self):
        """tests if save works"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """tests if dictionary works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
