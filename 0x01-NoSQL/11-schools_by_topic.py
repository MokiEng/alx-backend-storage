#!/usr/bin/env python3
""" task 11's module """


def schools_by_topic(mongo_collection, topic):
    """
    Get a list of schools that have a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection.
        topic (str): The topic to search for.

    Returns:
        list: A list of school documents matching the topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
