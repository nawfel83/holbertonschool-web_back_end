#!/usr/bin/env python3
"""Module that inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    
    Args:
        mongo_collection: pymongo collection object
        **kwargs: keyword arguments for the new document
    
    Returns:
        The new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
