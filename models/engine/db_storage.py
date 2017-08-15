#!/usr/bin/python3

import os
from sqlalchemy import create_engine

class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        self.__engine('mysql+mysqldb://{}:{}@{}/{}'
                      .format(os.getenv('HBNB_MYSQL_USER'),
                              os.getenv('HBNB_MYSQL_PWD'),
                              os.getenv('HBNB_MYSQL_HOST'),
                              os.getenv('HBNB_MYSQL_DB')))
        def all(self, cls=None):
            print("All")

        def new(self, obj):
            print("new")

        def save(self):
            print("save")

        def delete(self, obj=None):
            print("delete")

        def reload(self):
            print("reload")

        
