#!/usr/bin/env python3
""" Python file that contains a <BasicCache> class"""
from typing import Union
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    <BasicCache> class that inherits
    from <BaseCaching> and is a caching system
    """
    def put(self, key, item):
        """
        Must assign to the dictionary
        self.cache_data the item value
        for the key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data
        linked to key
        """
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
