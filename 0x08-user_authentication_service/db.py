#!/usr/bin/env python3
"""
database file
"""

from user import Base, User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, update
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

    def find_user_by(self, **kwargs) -> User:
        """ method that find a user """
        return self._session.query(User).filter_by(**kwargs).one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Locates the user to update, then will update the user’s
        attributes as passed in the method’s arguments and commit
        changes to the database.
        Args:
        ----
            user_id
            arbitrary keyworded arguments
        Returns:
        -------
            None
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in User.__table__.columns:
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
