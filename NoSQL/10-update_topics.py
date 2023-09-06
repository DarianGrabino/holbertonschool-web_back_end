#!/usr/bin/env python3
"""Change school topics"""
from pymongo.collection import Collection


def update_topics(mongo_collection: Collection, name: str, topics: list):
    """changes all topics of a school document based on the name"""
    filter_query = {"name": name}
    update_query = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(filter_query, update_query)
    return result.modified_count
