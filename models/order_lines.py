#!/usr/bin/python3
""" holds class OrderLine"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship


class OrderLine(BaseModel, Base):
    """Representation of OrderLine """
    __tablename__ = 'order_lines'
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes OrderLine"""
        super().__init__(*args, **kwargs)
