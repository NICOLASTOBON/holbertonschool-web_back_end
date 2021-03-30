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
            if path in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ header of authorization """
        if request:
            return request.headers.get('Authorization')
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ get current user"""
        return None
