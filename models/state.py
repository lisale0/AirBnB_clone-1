#!/usr/bin/python3
"""
State Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class handles all application states"""
    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
          __tablename__ = 'states'
          name = Column(String(128), nullable=False)
          cities = relationship("City", backref="state")
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
