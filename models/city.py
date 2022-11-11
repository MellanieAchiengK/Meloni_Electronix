#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    country_id = Column(Integer, ForeignKey('cuontries.id'), nullable=False)
    users = relationship("User", backref="users",
                         cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
