#!/usr/bin/env python3
""" Basic Authorization """

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
