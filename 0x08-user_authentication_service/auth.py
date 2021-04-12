#!/usr/bin/env python3
"""
authorization file
"""

import bcrypt


def _hash_password(password: str) -> str:
    """ function that tranform a string to hash """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
