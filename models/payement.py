#!/usr/bin/python3
""" holds class Payement"""
from datetime import datetime
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer, Numeric


class Payement(BaseModel, Base):
    """Representation of Payement """
    __tablename__ = 'payements'
    card_numer = Column(String(60), nullable=True)
    paid_at = Column(DateTime, default=datetime.utcnow)
    amount = Column(Numeric(10, 2), nullable=False),
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False,
                     comment="customer id")

    def __init__(self, *args, **kwargs):
        """initializes payement"""
        super().__init__(*args, **kwargs)
