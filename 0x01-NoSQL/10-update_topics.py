#!/usr/bin/env python3
""" Write a Python function that changes all topics of a school
    document based on the name:
"""


def update_topics(mongo_collection, name, topics):
    """ changes topic of a collection document"""
    filterBy = {"name": name}
    update = {$set: {"topics": topics}}
    return mongo_collection.update_many(fiterBy, update)
