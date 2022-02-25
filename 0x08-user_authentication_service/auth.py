#!/usr/bin/env python3
""" Auth module """
from db import DB
from user import User
import bcrypt
import uuid.3


def _hash_password(password: str) -> bytes:
    """
    _hash_password method
    Args:
        password
    Return:
        bytes
    """
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())

def _generate_uuid() -> str:
    """
    _generate_uuid method
    Return:
        String
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """
        Check if the request has
        correct credentials
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(str.encode(password), user.hashed_password)
        except Exception:
            return False
