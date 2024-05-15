#!/usr/bin/env python3
"""Basic authorization for the api
"""


from api.v1.auth.auth import Auth


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
