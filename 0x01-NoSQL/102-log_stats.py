#!/usr/bin/env python3
""" task 15's module."""
from pymongo import MongoClient


def get_log_stats(mongo_collection):
    """Count the total number of logs."""
    total_logs = mongo_collection.count_documents({})

    method_counts = {}
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        method_counts[method] = count

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(mongo_collection.aggregate(pipeline))

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")
    print("IPs:")
    for ip in top_ips:
        print(f"    {ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    get_log_stats(nginx_collection)
