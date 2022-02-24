#!/usr/bin/env python3
""" Auth module """
from db import DB
from user import User
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    _hash_password method
    Args:
        password
    Return:
        bytes
    """
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        register_user method
        Args:
            email
            password
        Return:
            User
        """
        try:
            self._db.find_user_by(email=email)
        except Exception:
            return self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError("User {} already exists".format(email))
