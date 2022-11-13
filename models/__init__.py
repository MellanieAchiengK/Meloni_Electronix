#!/usr/bin/python3
"""
initialize the models package
"""

from .db import Db
storage = Db()
storage.reload()
