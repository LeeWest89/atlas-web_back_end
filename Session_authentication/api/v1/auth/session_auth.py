#!/usr/bin/env python3
"""Session authorization for the api
"""


from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """SessionAuth class, inherting from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creating a unique session_id then tying it the the user_id"""
        if type(user_id) != str or user_id is None:
            return (None)

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return (session_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Getting user_id by using session_id"""
        if type(session_id) != str or session_id is None:
            return (None)

        return (self.user_id_by_session_id.get(session_id))
