#!/usr/bin/env python3
""" Python file that contains a class to manage the API authentication """
from api.v1.auth.auth import Auth
import re


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        """
        if not authorization_header or type(authorization_header) is not str:
            return None
        header = authorization_header.split(' ')
        return (None if not bool(re.search('^Basic ', authorization_header))
                else header[1])