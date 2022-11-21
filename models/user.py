#!/usr/bin/python3
""" holds class User"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from hashlib import md5
#from flask_login import UserMixin


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    phone1 = Column(String(25), nullable=True)
    phone2 = Column(String(25), nullable=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    adresses = relationship("Address", backref="address")
    orders = relationship("Order", backref="user")
    payements = relationship("Payement", backref="user")
    authentification = Column(Boolean, default=False)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
    