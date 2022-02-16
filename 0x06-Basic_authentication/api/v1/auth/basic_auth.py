#!/usr/bin/env python3
""" Python file that contains a class to manage the API authentication """
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64
import re


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if not authorization_header or type(authorization_header) is not str:
            return None
        header = authorization_header.split(' ')
        return (None if not bool(re.search('^Basic ', authorization_header))
                else header[1])

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        returns the decoded value of a Base64
        string base64_authorization_header
        """
        if (not base64_authorization_header or
                type(base64_authorization_header) != str):
            return None
        try:
            msg = base64.b64decode(base64_authorization_header.encode('utf-8'))
            return msg.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        returns the user email and password
        from the Base64 decoded value
        """
        if (not decoded_base64_authorization_header
                or type(decoded_base64_authorization_header) != str):
            return (None, None)
        credendials = decoded_base64_authorization_header.split(':', 1)
        return (credendials[0], credendials[1]) if ":" in\
            decoded_base64_authorization_header else (None, None)

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """
        returns the User instance based
        on his email and password.
        """
        if not user_email or not isinstance(user_email, str)\
           or not user_pwd or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            if not users:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Fully protected API with a Basic Authentication
        """
        try:
            header = self.authorization_header(request)
            base64header = self.extract_base64_authorization_header(header)
            decodebase64header = self.decode_base64_authorization_header(
                base64header)
            user_email, user_pwd = self.extract_user_credentials(
                decodebase64header)
            return self.user_object_from_credentials(user_email, user_pwd)
        except Exception:
            return None
