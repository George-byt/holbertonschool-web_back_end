#!/usr/bin/env python3
""" Python file about 0x05. Personal data project """
import bcrypt


def hash_password(password: str) -> bytes:
    """
    hash_password()
    encript password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """encrypt password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
