#!/usr/bin/env python3
"""lists all documents in a collection"""


def list_all(mongo_collection):
    """Function to list all documents"""
    return (mongo_collection.find())
