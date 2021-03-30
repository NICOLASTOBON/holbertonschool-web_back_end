#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth """
        if path and excluded_paths:
            if path[-1] != '/':
                path += '/'
            for pth in excluded_paths:
                if path == pth:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ header of authorization """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ get current user"""
        return None
