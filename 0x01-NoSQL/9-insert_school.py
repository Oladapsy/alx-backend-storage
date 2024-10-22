#!/usr/bin/env python3
""" Write a Python function that inserts a new document
    in a collection based on kwargs:
"""


def insert_school(mongo_collection, **kwargs):
    """ insert a new doc ina collection based on kwargs"""
    for k, v in kwargs.item():
        mongo_collection.insert({k: v})
