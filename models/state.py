#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
else:
    class State(BaseModel):
        """ State class """
        name = ""

        @property
        def cities(self):
            from models import storage
            cities = storage.all(City)
            city_l = [obj for obj in cities.values()
                      if obj.state_id == self.id]
            return city_l
