#!/usr/bin/python3
""" This is the test module for Base model. """

import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_Storoge(unittest.TestCase):
    """ This class test The base Model."""

    def test_instance(self):
        """ This method test the instance of
        the base model.
        """

        obj = FileStorage()
        obj.save()
        self.assertIsInstance(obj, FileStorage)
        obj_dict = models.storage.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn("BaseModel.{}".format(obj.id), obj_dict)

    def test_save(self):
        """ This method test the string representation of
        the base model.
        """

        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        dic = models.storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), dic)

    def test_new(self):
        """ This method test the attributes of
        the base model.
        """

        obj = BaseModel()
        models.storage.new(obj)
        dic = models.storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), dic)

    def test_reload(self):
        """ This method test the attributes of
        the base model.
        """

        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        models.storage.reload()
        dic = models.storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), dic)
