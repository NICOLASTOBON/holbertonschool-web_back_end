#!/usr/bin/env python3
""" Basic Authorization """

import base64
from typing import Tuple
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Authorization"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Basic - Base64 part """
        if authorization_header and isinstance(authorization_header, str):
            if 'Basic ' in authorization_header:
                if authorization_header[0:6] == 'Basic ':
                    return authorization_header[6:]
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Base64 decode """
        if base64_authorization_header and \
                isinstance(base64_authorization_header, str):
            try:
                return base64.b64decode(base64_authorization_header).decode()
            except base64.binascii.Error:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        User credentials
        Return: tuple
        """
        if decoded_base64_authorization_header and \
                isinstance(decoded_base64_authorization_header, str):
            if ':' in decoded_base64_authorization_header:
                return tuple(decoded_base64_authorization_header.split(':'))
        return (None, None)
