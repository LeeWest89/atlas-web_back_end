#!/usr/bin/env python3
"""Session authorization for the api
"""


from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class SessionAuth(Auth):
    """SessionAuth class, inherting from Auth"""
    pass
