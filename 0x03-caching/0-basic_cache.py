#!/usr/bin/env python3
""" Python file that contains a <BasicCache> class"""
from typing import Union
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Comment:
    """
    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
