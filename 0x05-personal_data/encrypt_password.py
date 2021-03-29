#!/usr/bin/env python3
""" Encrypting passwords """

import bcrypt
from typing import ByteString


def hash_password(password: str) -> ByteString:
    """ return a password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
