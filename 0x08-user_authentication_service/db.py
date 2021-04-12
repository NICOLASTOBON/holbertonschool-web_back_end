#!/usr/bin/env python3
"""
database file
"""

from user import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base


class DB:
    """ Database class"""
    def __init__(self):
        """ method constructor that create a connection"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ method that create a session"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """methood that create new user """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs):
        """ method that find a user """
        if not kwargs:
            raise InvalidRequestError

        properties = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in properties:
                raise InvalidRequestError

        return self._session.query(User).filter_by(**kwargs).one()
