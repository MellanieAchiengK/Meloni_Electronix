#!/usr/bin/python3
"""
initialize the models package
"""

#from models.db import Db
from .db import Db
storage = Db()
storage.reload()
