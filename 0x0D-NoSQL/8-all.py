#!/usr/bin/env python3
"""
Python file tha contains
a Python function
"""


def list_all(mongo_collection):
    """
    Python function that lists
    all documents in a collection
    """
    l = mongo_collection.find()
    return l if l else []
