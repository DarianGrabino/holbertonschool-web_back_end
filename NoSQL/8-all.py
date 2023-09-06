#!/usr/bin/env python3
"""List all documents"""
import pymongo

def list_all(mongo_collection):
    """lists all documents in a collection"""
    list_documents = mongo_collection.find()
    if list_documents:
        return list_documents
    else:
        return []
