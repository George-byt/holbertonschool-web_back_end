#!/usr/bin/env python3
""" Python file that contains a class to manage the API authentication """
from flask import request
from typing import List, TypeVar

class Auth:
    """
    Auth class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Return:
            False - path and excluded_paths
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Return:
            None - request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return:
            None - request
        """
        return None
