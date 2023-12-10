#!/usr/bin/python3
""" This serializes instances to a JSON file
and deserializes JSON file to instances
"""


import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This method returns the dictionary __objects.
        """

        return self.__objects

    def new(self, obj):
        """ This method sets in __objects the
        obj with key <obj class name>.id
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ This method  serializes __objects to the
        JSON file (path: __file_path).
        """

        data = {}
        for key in self.__objects:
            data[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """ This method deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception
        should be raised)
        """

        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, o_id = key.split(".")
                    o_class = globals()[class_name]
                    obj = o_class(**value)
                    self.new(obj)
        except Exception:
            pass
