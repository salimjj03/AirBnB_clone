#!/usr/bin/python3
""" This is the class BaseModel that defines all common
    attributes/methods for other classes.
    """


import uuid
import datetime
import models


class BaseModel:
    """ This is the Base class. """

    def __init__(self, *args, **kwargs):
        """ This method Public instance attributes. """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'
                            )
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = datetime.datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """ This is the str Method. """

        return "[{}]({}){}".format(
                type(self).__name__,
                self.id, self.__dict__
                )

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime.
        """

        self.updated_at = datetime.datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance.
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
