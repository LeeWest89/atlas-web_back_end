#!/usr/bin/env python3
""" Authorization for the api
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Class for Authorization"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public Method for authorization"""
        return (False)

    def authorization_header(self, request=None) -> str:
        """Public Method for authorization"""
        return (None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Public Method for authorization"""
        return (None)
