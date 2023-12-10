#!/usr/bin/python3
""" This is the User Model which inherit from
The BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ This is the User Model which inherit from
    The BaseModel.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
