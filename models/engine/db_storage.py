#!/usr/bin/python3
"""Module that defines a class that works an engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Class that defines an engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        user = getenv("HBNB_MYSQL_USER")
        pswd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        d_bs = getenv("HBNB_MYSQL_DB")
        envr = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(user, pswd, host, d_bs),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """query on the current database session"""
        dicty = {}
        if cls is not None:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + "." + obj.id
                dicty[key] = obj
        return dicty

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
