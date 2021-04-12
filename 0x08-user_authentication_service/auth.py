#!/usr/bin/env python3
"""
authorization file
"""

import bcrypt


def _hash_password(password: str) -> str:
    """ function that tranform a string to hash """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()
