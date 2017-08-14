#!/usr/bin/python3
"""
City Class from Models Module
"""


import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.state import State

class City(BaseModel):
    """City class handles all application cities"""

    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ''
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)
