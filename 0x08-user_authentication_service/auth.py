#!/usr/bin/env python3
"""
authorization file
"""

import uuid
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ method constructor """
        self._db = DB()
        self.__id = None

    def register_user(self, email: str, password: str) -> User:
        """ method that register a new user """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hash_pwd = _hash_password(password)
            return self._db.add_user(email=email, hashed_password=hash_pwd)

    def valid_login(self, email: str, password: str) -> bool:
        """ method that check if the user is correct """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                    password.encode(), user.hashed_password.encode()
                )
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """method that create a new Session ID """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ method that get a user by session ID"""
        if not session_id:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ method that destroy a session """
        if not user_id:
            return None

        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except NoResultFound:
            return None


def _hash_password(password: str) -> str:
    """ function that tranform a string to hash """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def _generate_uuid() -> str:
    """ function that generate a UUID """
    return str(uuid.uuid4())
