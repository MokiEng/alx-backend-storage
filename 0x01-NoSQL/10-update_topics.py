#!/usr/bin/env python3
'''Task 10's module.
'''


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document based on the school's name.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to be set for the school.

    Returns:
        None
    """
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
