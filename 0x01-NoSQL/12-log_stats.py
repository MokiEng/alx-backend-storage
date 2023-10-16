#!/usr/bin/env python3
"""
Script to provide statistics about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stats():
    """a Python script that provides some stats about
    Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    total_logs = logs_collection.count_documents({})

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in http_methods:
        count = logs_collection.count_documents({"method": method})
        method_counts[method] = count
    status_check_count = logs_collection.count_documents(
            {"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
