#!/usr/bin/python3
""" holds class Product"""
from .base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """Representation of Product """
    __tablename__ = 'products'
    name = Column(String(128), nullable=False)
    image = Column(String(128), nullable=True)
    selling_price = Column(Numeric(10, 2), nullable=False, default=0)
    cost_price = Column(Numeric(10, 2), nullable=False, default=0)
    description = Column(String(1024), nullable=True)
    quantity = Column(Integer, nullable=False, default=0)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    order_lines = relationship("OrderLine", backref="orderLine",
                               cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes product"""
        super().__init__(*args, **kwargs)
