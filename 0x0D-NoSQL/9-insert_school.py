#!/usr/bin/env python3
"""
Python file tha contains
a Python function
"""


def insert_school(mongo_collection, **kwargs):
    """
    Python function that inserts
    a new document in a collection
    based on kwargs
    """
    x = mongo_collection.insert_one(kwargs)
    return x.inserted_id
