#!/usr/bin/python3
""" holds class Photo"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer


class Photo(BaseModel, Base):
    """Representation of Photo"""
    __tablename__ = 'photos'
    link = Column(String(128), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes payement"""
        super().__init__(*args, **kwargs)
