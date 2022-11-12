#!/usr/bin/python3
""" holds class Country"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Country(BaseModel, Base):
    """Representation of Country """
    __tablename__ = 'countries'
    iso2 = Column(String(2), nullable=False)
    name = Column(String(128), nullable=False)
    nicename = Column(String(128), nullable=False)
    iso3 = Column(String(128), nullable=False)
    numcode = Column(Integer(), nullable=False)
    phonecode = Column(Integer, nullable=False)
    cities = relationship("City", backref="country",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes country"""
        super().__init__(*args, **kwargs)
