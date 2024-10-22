#!/usr/bin/env python3
""" a Python script that provides some stats about Nginx
    logs stored in MongoDB:
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """ a Python script that provides some stats about Nginx
        logs stored in MongoDB:
    """

    client = MongoClient(host="localhost", port=27017)
    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})
    print(F"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(F"\tmethod {method}: {count}")

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(F"{status_check} status check")
