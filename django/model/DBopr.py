__author__ = 'zice'

from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['test']
collection = db['newfans']


def get_fan_by_uid(fan_id):
    fan = collection.find_one({"uid":fan_id})
    return fan


# s = get_fan_by_uid("1136750677")
# print s["name"]