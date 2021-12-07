#!/usr/bin/env python3
"""
"""

from pymongo import MongoClient


def find_by(coll, field, value):
    """
    Returns the list of collections with specific value
    """
    return list(coll.find({field: value}))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    nb_logs = list(logs.find())
    print(f"""{len(nb_logs)} logs
Methods:
    method GET: {len(find_by(logs, 'method', 'GET'))}
    method POST: {len(find_by(logs, 'method', 'POST'))}
    method PUt: {len(find_by(logs, 'method', 'PUT'))}
    method PATCH: {len(find_by(logs, 'method', 'PATCH'))}
    method DELETE: {len(find_by(logs, 'method', 'DELETE'))}
{len(find_by(logs, 'path', '/status'))} status check""")

