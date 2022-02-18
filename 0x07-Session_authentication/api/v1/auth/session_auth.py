##!/usr/bin/env python3
""" Python file that contains the SessionAuth class """
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    Class: SessionAuth

    It's the first step for creating a new authentication
    mechanism:

        => validate if everything inherits correctly whitout
        any overloading

        => validate the "switch" by using environment variables
    """
    pass
