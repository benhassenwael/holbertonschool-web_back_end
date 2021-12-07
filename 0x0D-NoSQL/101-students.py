#!/usr/bin/env python3
""" 0x0D-NoSQL """

from collections import OrderedDict


def top_students(mongo_collection):
    """
    Return all students sorted by average score
    """

    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {"_id": "$_id", "name": { "$first": "$name"},
                    "averageScore":{"$avg": "$topics.score"}
                    }},
#        {"$addFields": {"name": "fdsf"}},
        {"$sort": OrderedDict([("averageScore", -1), ("_id", -1)])}
        ]

    return list(mongo_collection.aggregate(pipeline))
