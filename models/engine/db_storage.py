#!/usr/bin/python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
    from models.place import PlaceAmenity
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """ DBStorage is the engine for the MySQL database"""
    __engine = None
    __session = None

    CNC = {
        'BaseModel': BaseModel,
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
    }
    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
        CNC['PlaceAmenity'] = PlaceAmenity

    def __init__(self):
        """engine and session is initialized"""
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
        """prints all the objects in the specified class none/ print all"""
        all_dict = {}
        if cls is not None:
            try:
                for instance in self.__session.query(DBStorage.CNC[cls]).all():
                    k = str(instance.__class__.__name__) + "."
                    + str(instance.id)
                    all_dict[k] = instance
            except:
                pass
        else:
            for k, v in DBStorage.CNC.items():
                if k != "PlaceAmenity" and k != "BaseModel":
                    try:
                        for instance in self.__session.query(v).all():
                            clss = str(instance.__class__.__name__)
                            k = clss + "." + str(instance.id)
                            all_dict[k] = instance
                    except:
                        pass
        return all_dict

    def new(self, obj):
        """adds a new object to the MYSQL database"""
        self.__session.add(obj)

    def save(self):
        """ saves all changes made in the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes specified object"""
        if (obj):
            self.__session.delete(obj)

    def reload(self):
        """ loads session and save to self.__session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine)
        self.__session = scoped_session(session)
