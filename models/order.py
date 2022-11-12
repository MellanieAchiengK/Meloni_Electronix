#!/usr/bin/python3
""" holds class Order"""
from datetime import datetime
from models.base_model import BaseModel, Base
from models.city import City
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship


class Order(BaseModel, Base):
    """Representation of Order """
    __tablename__ = 'orders'
    order_number = Column(String(60), nullable=False)
    ordered = Column(DateTime, default=datetime.utcnow)
    shipped = Column(DateTime)
    status = Column(Integer(),
                    comment="1=New, 2=Hold, 3=Shipped, 4=delivered, 5=closed")
    total = Column(Integer, nullable=False)
    address_id = Column(Integer, ForeignKey("adresse.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("adresse.id"), nullable=False,
                     comment="customer id")
    order_lines = relationship("orderLine", secondary="order_lines",
                               backref='order',
                               cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes order"""
        super().__init__(*args, **kwargs)
