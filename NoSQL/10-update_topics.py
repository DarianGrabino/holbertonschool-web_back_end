#!/usr/bin/env python3
"""Change school topics"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    change all topics of a school document based on the name
    Args:
        mongo_collection: collection object
        name (str) : name of the school to be updated
        topics ([str]): list with topic names
    Return:
        number of modified documents
    """
    filter_query = {"name": name}
    update_query = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(filter_query, update_query)
    return result.modified_count
