#!/usr/bin/python3
""" holds class Category"""
from datetime import datetime
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """Representation of Category"""
    __tablename__ = 'categories'
    name = Column(String(128), nullable=False)
    image = Column(String(128), nullable=True)
    """ products = relationship("Product", backref='category',
                            cascade="all, delete, delete-orphan")
 """
    def __init__(self, *args, **kwargs):
        """initializes category"""
        super().__init__(*args, **kwargs)
