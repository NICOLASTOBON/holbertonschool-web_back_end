#!/usr/bin/env python3
""" Session Authorization """

import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ session class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ method that create a session """
        if user_id and isinstance(user_id, str):
            id = str(uuid.uuid4())
            self.user_id_by_session_id[id] = user_id
            return id
        return None
