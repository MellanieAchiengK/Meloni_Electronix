#!/usr/bin/python3
"""
Contains the class Db
"""

from models.base_model import BaseModel, Base
from models.address import Address
from models.category import Category
from models.city import City
from models.country import Country
from models.order_lines import OrderLine
from models.order import Order
from models.payement import Payement
from models.photo import Photo
from models.product import Product
from models.user import User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


classes = {
            "Adresse": Address,
            "Category": Category,
            "City": City,
            "Country": Country,
            "OrderLine": OrderLine,
            "Order": Order,
            "Payement": Payement,
            "Photo": Photo,
            "Product": Product,
            "User": User
        }


class Db:
    """interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        ME_MYSQL_USER = getenv('ME_MYSQL_USER')
        ME_MYSQL_PWD = getenv('ME_MYSQL_PWD')
        ME_MYSQL_HOST = getenv('ME_MYSQL_HOST')
        ME_MYSQL_DB = getenv('ME_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(ME_MYSQL_USER,
                                             ME_MYSQL_PWD,
                                             ME_MYSQL_HOST,
                                             ME_MYSQL_DB))
        """ self.__engine = create_engine('sqlite:///melani_electronique.db', echo = True) """

    def all(self, cls=None):
        """ query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = str(obj.__class__.__name__) + '.' + str(obj.id)
                    new_dict[key] = obj
        return (new_dict)
    
    def get_id(self, cls=None, motif=None):
        #print("motif rechercher: {}".format(motif))
        dic = self.all(cls).values()
        liste = []
        for loop in dic:
            liste.append((loop.to_dict().get('id'), loop.to_dict().get('name')))
        
        for loop in liste:
            if loop[1] == motif:
                return loop
        return None

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def get(self, cls, id):
        """Retrieves one object by ID in the current database session"""
        return self.__session.query(cls).get(id)

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
