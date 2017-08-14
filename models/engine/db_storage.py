#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(os.getnev('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')))

    def all(self, cls=None):
        Session  = sessionmaker(bind=self.__engine)
        self.__session = Session()
    
    def new(self, cls=None):
        print("new")

    def save(self):
        print("save")
