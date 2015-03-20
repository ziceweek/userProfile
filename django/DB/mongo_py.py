__author__ = 'zice'
import os
import json
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['test']
collection_fansWeibo = db['fansWeibo']

f = open("/run/media/zice/DM/userProfile/A1weibo/"+"1008912684.txt")
weibo_json = f.readlines()
i = 0
for line in weibo_json:
    try:
        s = json.loads(line)
        print collection_fansWeibo.update({"fans_id":"1008912684"}, {"$push":{"weibos": {"$each": s["statuses"]}}}, True)
        print s["statuses"]
        i += 1
    except Exception :
        print "error"

# weibo_json = f.readline()
# try:
#     s = json.loads(weibo_json)
#     print collection_fansWeibo.update({"fans_id":"789"}, {"$push":{"weibos": {"$each": s["statuses"]}}}, True)
#     # print s["statuses"][0]
# except Exception :
#     print "error"

for a in collection_fansWeibo.find():
    # print a
    print "----"
    if "fans_id" in a:
        print a["fans_id"]