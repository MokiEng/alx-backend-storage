#!/usr/bin/env python3
""" 8-main """


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection.

    Returns:
        list: A list of all documents in the collection.
    """
    return [doc for doc in mongo_collection.find()]
