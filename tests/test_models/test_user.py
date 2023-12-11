#!/usr/bin/python3
""" This is the test module for Base model. """

import unittest
from models.user import User


class Test_Storoge(unittest.TestCase):
    """ This class test The base Model."""

    def test_instance(self):
        """ This method test the instance of
        the base model.
        """

        obj = User()
        self.assertIsInstance(obj, User)

    def test_attribute(self):
        """ This method test the string representation of
        the base model.
        """

        obj = User()

        obj.email = "string"
        obj.password = "string"
        obj.first_name = "string"
        obj.last_name = "string"

        self.assertEqual(obj.email, "string")
        self.assertEqual(obj.password, "string")
        self.assertEqual(obj.first_name, "string")
        self.assertEqual(obj.last_name, "string")

    def test_value(self):
        """ This method test the attributes of
        the base model.
        """

        obj = User()

        obj.email = 1
        obj.password = [2, 2]
        obj.first_name = {}

        self.assertEqual(obj.email, 1)
        self.assertEqual(obj.password, [2, 2])
        self.assertEqual(obj.first_name, {})
