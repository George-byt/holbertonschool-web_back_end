#!/usr/bin/env python3
"""
Writing strings to Redis, Reading from Redis and recovering original type,
Incrementing values, Storing lists, Retrieving lists 
"""
from typing import Union
import redis
import uuid


class Cache():
    """
    Cache class
    """

    def __init__(self):
        """
        __init__ method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        The method should generate a random key,
        store the input data in Redis using the key and
        return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
