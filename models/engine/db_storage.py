#!/usr/bin/python3
"""DBStorage - States and Cities"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place


class DBStorage:
    """New engine"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return a dictionary"""
        sd = {}
        All_cls = ['State', 'City', 'User', 'Place', 'Review', 'Amenity']
        if cls:
            obj = self.__session.query(cls).all()
            for o in obj:
                k = "{}.{}".format(type(o).__name__, o.id)
                sd[k] = o
        else:
            for cl in All_cls:
                obj = self.__session.query(eval(cl)).all()
                for o in obj:
                    k = "{}.{}".format(type(o).__name__, o.id)
                    sd[k] = o
        return sd

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        ss = scoped_session(self.__session)
        self.__session = ss()

    def close(self):
        """close"""
        self.__session.close()
