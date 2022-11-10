#!/usr/bin/python3
"""
Contains the class Db
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class Db:
    """interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = 'root'
        HBNB_MYSQL_PWD = 'phpmyadmin'
        HBNB_MYSQL_HOST = 'localhost'
        HBNB_MYSQL_DB = 'crud'
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))

    # def all(self, cls=None):
        """query on the current database session"""
        """ new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict) """

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

    # def count(self, cls=None):
        """Returns the number of objects in storage matching the given class"""
        """ if cls is not None:
            return self.__session.query(cls).count()
        return len(self.all()) """

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
