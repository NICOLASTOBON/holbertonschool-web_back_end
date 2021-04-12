#!/usr/bin/env python3
"""
authorization file
"""

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


def _hash_password(password: str) -> str:
    """ function that tranform a string to hash """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
