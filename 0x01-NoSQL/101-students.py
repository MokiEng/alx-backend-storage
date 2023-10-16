#!/usr/bin/env python3
"""task 14's module """


def top_students(mongo_collection):
    """a Python function that returns all students
    sorted by average score
    """
    pipeline = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    students = list(mongo_collection.aggregate(pipeline))
    return students
