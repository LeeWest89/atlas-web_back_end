#!/usr/bin/env python3
"""Basic authorization for the api
"""


from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class, inherting from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Finds the Base64 in Authorization"""
        if authorization_header is None:
            return (None)

        if type(authorization_header) != str:
            return(None)

        if not authorization_header.startswith('Basic '):
            return(None)

        return (authorization_header.split(' ')[1])

    def decode_base64_authorization_header(
                                           self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Decodes the Base64 String"""
        if base64_authorization_header is None:
            return (None)

        if type(base64_authorization_header) != str:
            return(None)

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded = decoded_bytes.decode('utf-8')
            return (decoded)
        except Exception:
            return (None)

    def extract_user_credentials(
                                 self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Extractes user credentials"""
        if decoded_base64_authorization_header is None:
            return (None, None)

        if type(decoded_base64_authorization_header) != str:
            return(None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        email, pswd = decoded_base64_authorization_header.split(':', 1)
        return (email, pswd)

    def user_object_from_credentials(
                                     self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Returns user instance"""

        if user_email is None or type(user_email) != str:
            return (None)

        if user_pwd is None or type(user_pwd) != str:
            return (None)

        try:
            user = User.search({'email': user_email})
        except Exception:
            return (None)

        if not user:
            return (None)

        if not user[0].is_valid_password(user_pwd):
            return (None)

        return (user[0])

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the user"""
        authorization = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(authorization)
        decoded = self.decode_base64_authorization_header(b64)
        email, pswd = self.extract_user_credentials(decoded)
        user = self.user_object_from_credentials(email, pswd)

        return(user)
