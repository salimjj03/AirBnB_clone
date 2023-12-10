#!/usr/bin/python3
""" This is the test model for BaseModel."""

import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_baseclass(unittest.TestCase):
    """ This is the test model for BaseModel."""

    pass


if __name__ == "__main__":
    unittest.testmode()
