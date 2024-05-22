#!/usr/bin/env python3
"""Auth module
"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hashes the password"""
    return (bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))


def _generate_uuid() -> str:
    """Generates uuid"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Sets up new users"""
        try:
            user = self._db.find_user_by(email=email)

            if user:
                raise ValueError("User {} already exists".format(email))

        except NoResultFound:
            pass

        return (self._db.add_user(email, _hash_password(password)))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate logins"""
        try:
            user = self._db.find_user_by(email=email)

            if user and bcrypt.checkpw(password.encode('utf-8'),
                                       user.hashed_password):
                return (True)

            else:
                return (False)

        except NoResultFound:
            return (False)

    def create_session(self, email: str) -> str:
        """Creates a session id for the user"""
        try:
            user = self._db.find_user_by(email=email)
            s_id = _generate_uuid()
            self._db.update_user(user.id, session_id=s_id)
            return (s_id)

        except NoResultFound:
            return (None)

    def get_user_from_session_id(self, session_id: str) -> User:
        """Returns User or None based on session_id"""
        if session_id is None:
            return (None)

        try:
            user = self._db.find_user_by(session_id=session_id)
            return (user)

        except NoResultFound:
            return (None)

    def destroy_session(self, user_id: int) -> None:
        """Set session_id to None to destory session"""
        try:
            self._db.update_user(user_id, session_id=None)

        except NoResultFound:
            pass

        return (None)

    def get_reset_password_token(self, email: str) -> str:
        """Returns a reset_token"""
        try:
            user = self._db.find_user_by(email=email)

        except NoResultFound:
            raise ValueError

        reset_token = str(uuid.uuid4())
        self._db.update_user(user.id, reset_token=reset_token)

        return (reset_token)
