#!/usr/bin/python3

import os
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.engine import PARAM

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        try:
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                          .format(os.getenv('HBNB_MYSQL_USER'),
                                  os.getenv('HBNB_MYSQL_PWD'),
                                  os.getenv('HBNB_MYSQL_HOST'),
                                  os.getenv('HBNB_MYSQL_DB')))
            """
            print(os.getenv('HBNB_MYSQL_USER'))
            print(os.getenv('HBNB_MYSQL_PWD'))
            print(os.getenv('HBNB_MYSQL_HOST'))
            print(os.getenv('HBNB_MYSQL_DB'))
            """
        except:
            print("Environment Variables not populated")
        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        print("all")

    def new(self, obj):
        print("new")
        
        """
        self.__session.add(obj)
        print("Printing Obbject {} : name: {}".format(obj, obj.name))
        """
        print(PARAM)

    def save(self):
        print("save")

    def delete(self, obj=None):
        print("delete")

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_factory)
        self.__session = Session()

