#!/usr/bin/env python3
"""a Python function that lists all documents in a collection:"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """list all document in a collection"""
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []
    return documents
