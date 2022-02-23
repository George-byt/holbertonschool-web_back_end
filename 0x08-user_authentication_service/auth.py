#!/usr/bin/env python3
""" Auth module """
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
