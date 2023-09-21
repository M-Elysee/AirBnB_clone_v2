#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
import sqlalchemy
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
        Represents a user database.

        Inherits from Base and links to table users.

        Attributes:
            __tablename__ (str): Name table to store users.
            email: (String): User's email address.
            password (String): User's password.
            first_name (String): User's first name.
            last_name (String): The user's last name.
            places (relationship): User-Place relationship.
            reviews (relationship): The User-Review relationship.
    """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128))
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
