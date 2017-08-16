#!/usr/bin/python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place, PlaceAmenity
from models.review import Review
from models.state import State
from models.user import User

class DBStorage:
    __engine = None
    __session = None

    CNC = {
        'BaseModel': BaseModel,
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'PlaceAmenity': PlaceAmenity,
        'User': User
    }
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')))
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine)
        self.__session = session()
        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        sess = self.__session
        if cls is not None:
            print (cls)
            for instance in self.__session.query(DBStorage.CNC[cls]).all():
                print(instance)
        else:
            for k, v in DBStorage.CNC.items():
                if k != "PlaceAmenity" and k != "BaseModel":
                    print (v)
                
                    for instance in self.__session.query(v).all():
                        print(instance)
        

    def new(self, obj):
        print("New entered")
        print(obj)
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if (obj):
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine)
        self.__session = scoped_session(session)
