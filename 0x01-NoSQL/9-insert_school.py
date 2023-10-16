#!/usr/bin/env python3
""" task 9 module """


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection.
        **kwargs: Keyword arguments for the document to be inserted.

    Returns:
        str: The _id of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
