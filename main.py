from pymongo import MongoClient
import json
import os
import logging

logging.basicConfig(level=logging.INFO)


def get_mongo_client():
    mongo_uri = os.environ.get("MONGODB_URI")
    return MongoClient(mongo_uri)


def get_mongo_db():
    db = os.environ.get("MONGODB_DATABASE")
    return get_mongo_client()[db]


def get_campaigns():
    database = get_mongo_db()
    campaigns_col = database.campaigns
    return campaigns_col.find()


if __name__ == '__main__':
    for campaign in get_campaigns():
        print(campaign)
