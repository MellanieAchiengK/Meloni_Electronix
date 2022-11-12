#!/usr/bin/python3
""" holds class Address"""
from datetime import datetime
from models.base_model import BaseModel, Base
from models.city import City
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship


class Address(BaseModel, Base):
    """Representation of Address """
    __tablename__ = 'addresss'
    street = Column(String(60), nullable=True)
    zip_code = Column(String(10), nullable=True)
    status = Column(Integer(1),
                    comment="1=New, 2=Hold, 3=Shipped, 4=delivered, 5=closed")
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False,
                     comment="customer id")
    orders = relationship("Order", backref='address')

    def __init__(self, *args, **kwargs):
        """initializes address"""
        super().__init__(*args, **kwargs)
