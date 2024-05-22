#!/usr/bin/env python3
""" Authorization for the api
"""


from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Class for Authorization"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public Method for authorization of a path"""
        if not (path and excluded_paths):
            return (True)

        if not path.endswith('/'):
            path += '/'

        for e_path in excluded_paths:
            if e_path.endswith('/'):
                e_path = e_path[:-1]
            if path.startswith(e_path):
                return (False)

        return (True)

    def authorization_header(self, request=None) -> str:
        """Public Method for authorization"""
        if not request or 'Authorization' not in request.headers:
            return (None)

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Public Method for authorization"""
        return (None)

    s_name = os.getenv('SESSION_NAME', '_my_session_id')

    def session_cookie(self, request=None):
        """returns a cookie value from a request or None"""
        if request is None:
            return (None)
        return (request.cookies.get(self.s_name))
