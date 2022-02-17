#!/usr/bin/env python3
""" Python file that contains a class to manage the API authentication """
from os import getenv
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Return:
            True: if the path is not in the list of string excluded_paths
            False - path and excluded_paths
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        for element in excluded_paths:
            if "*" in element:
                return not(path.startswith(element.replace("*", "")))
        return not(path in excluded_paths or f'{path}/' in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """
        Return:
            None - request
        """
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return:
            None - request
        """
        return None

    def session_cookie(self, request=None):
        """
        Method that returns a cookie
        value from a request
        """
        if request is None:
            return None
        return request.cookies.get(getenv("SESSION_NAME"))\
            if getenv("SESSION_NAME") else None
