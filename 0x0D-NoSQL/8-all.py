#!/usr/bin/env python3
""" 0x0D-NoSQL """


def list_all(mongo_collection):
    """ List all documents in a collection """
    return list(mongo_collection.find())
