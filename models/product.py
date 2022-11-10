#!/usr/bin/python3
""" holds class Product"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """Representation of Product """
    __tablename__ = 'products'
    name = Column(String(128), nullable=False)
    price = Column(Integer, nullable=False, default=0)
    description = Column(String(1024), nullable=True)
    quantity = Column(Integer, nullable=False, default=0)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes product"""
        super().__init__(*args, **kwargs)

    @property
    def orderItems(self):
        """getter for list of orderitems instances related to the product"""
        order_list = []

        return order_list
