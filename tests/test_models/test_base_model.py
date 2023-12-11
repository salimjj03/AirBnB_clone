#!/usr/bin/python3
""" This is the test module for Base model. """

import unittest
from models.base_model import BaseModel


class Test_Base(unittest.TestCase):
    """ This class test The base Model."""

    def test_attrbt(self):
        """ This method test the attributes of
        the base model.
        """

        usr = BaseModel()
        usr.name = "salim"
        self.assertEqual(usr.name, "salim")

    def test_instance(self):
        """ This method test the instance of
        the base model.
        """

        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_str(self):
        """ This method test the string representation of
        the base model.
        """

        obj = BaseModel()
        output = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(obj.__str__(), output)

    def test_save(self):
        """ This method test the attributes of
        the base model.
        """

        obj = BaseModel()
        updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(updated_at, obj.updated_at)

    def test_to_dict(self):
        """ This method test the attributes of
        the base model.
        """

        obj = BaseModel()
        dic = obj.to_dict()
        self.assertIsInstance(dic, dict)
        self.assertIn('__class__', dic)
        self.assertIn('id', dic)
        self.assertIn('created_at', dic)
        self.assertIn('updated_at', dic)
