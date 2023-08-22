#!/usr/bin/python3
"""Module that defines a class that works an engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from os import getenv


class DBStorage:
    """Class that defines an engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        us = getenv("HBNB_MYSQL_USER")
        ps = getenv("HBNB_MYSQL_PWD")
        ho = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envr = getenv("HBNB_ENV")
        self.__engine = create_engine(f"mysql+mysqldb://{us}:{ps}@{ho}/{db}",
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
            data = self.__session.query(obj.__class__).filter_by(id=obj.id).first()
            self.__session.delete(data)

    def reload(self):
        """create all tables in the database and the session"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove method on the private session attribute"""
        self.__session.close()
