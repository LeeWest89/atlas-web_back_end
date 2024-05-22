#!/usr/bin/env python3
"""Auth module
"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hashes the password"""
    return (bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Sets up new users"""
        try:
            current_user = self._db.find_user_by(email=email)

            if current_user:
                raise ValueError("User {} already exists".format(email))

        except NoResultFound:
            pass

        return (self._db.add_user(email, _hash_password(password)))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate logins"""
        try:
            user = self . _db.find_user_by(email=email)

            if user and bcrypt.checkpw(password.encode('utf-8'),
                                       bcrypt.hashpw(password.encode('utf-8'),
                                       bcrypt.gensalt())):
                return (True)

            else:
                return (False)

        except NoResultFound:
            return (False)
