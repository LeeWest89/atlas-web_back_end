#!/usr/bin/env python3
"""Basic authorization for the api
"""


from api.v1.auth.auth import Auth
import base64


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
