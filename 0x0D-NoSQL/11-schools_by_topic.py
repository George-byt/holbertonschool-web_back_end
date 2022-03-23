#!/usr/bin/env python3
"""
Python file tha contains
a Python function
"""


def schools_by_topic(mongo_collection, topic):
    """
    Python function that returns the list
    of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
