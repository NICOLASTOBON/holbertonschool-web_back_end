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

    def _generate_uuid(self) -> str:
        """ function that generate a UUID """
        return str(uuid.uuid4())


def _hash_password(password: str) -> str:
    """ function that tranform a string to hash """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
