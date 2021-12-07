#!/usr/bin/env python3
""" 0x0D-NoSQL """


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
