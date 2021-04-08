#!/usr/bin/env python3
""" Expiratetion date """

import os
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """ Session expiration class """
    def __init__(self):
        """ method constructor """
        SESSION_DURATION = os.getenv('SESSION_DURATION')
        try:
            if SESSION_DURATION:
                self.session_duration = int(SESSION_DURATION)
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        method that create a new session authentication
        """
        session_id = super().create_session(user_id)
        if session_id:
            session_dict = {}
            date = datetime.now()
            session_dict['user_id'] = user_id
            session_dict['created_at'] = date

            self.user_id_by_session_id[session_id] = session_dict
            return session_id
        return None

    def user_id_for_session_id(self, session_id=None):
        """ method that return a User """
        if session_id is None:
            return None
        if self.user_id_by_session_id[session_id] is None:
            return None

        usr_inf = self.user_id_by_session_id.get(session_id)
        if not usr_inf:
            return None

        if self.session_duration <= 0:
            return usr_inf.get('user_id')

        # get date from session_dict
        created = usr_inf.get('created_at')
        if created is None:
            return None

        exp_dt = created + timedelta(seconds=self.session_duration)
        if exp_dt < datetime.now():
            return None
        return usr_inf.get('user_id')
