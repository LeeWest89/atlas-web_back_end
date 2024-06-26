#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats(nginx):
    """provides some stats about Nginx logs stored in MongoDB"""
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    logs = nginx.count_documents({})
    method_counts = {}

    for m in method:
        method_counts[m] = nginx.count_documents({'method': m})

    status_count = nginx.count_documents({'method': 'GET',
                                               'path': '/status'})

    print('{} logs'.format(logs))
    print('Methods:')

    for m, count in method_counts.items():
        print('\tmethod {}: {}'.format(m, count))

    print('{} status check'.format(status_count))


if __name__ == "__main__":
    log_stats(MongoClient('mongodb://127.0.0.1:27017').logs.nginx)
