__author__ = 'zice'
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['test']
collection_newfans = db['newfans']


f = open("/run/media/zice/DM/userProfile/A1weibo/"+"1008912684.txt")
weibo_json = f.readlines()
weibolist = []

for line in weibo_json:
    s = json.loads(line)
    weibolist.append(s["statuses"])

for weibo in weibolist:
    print weibo

# try:
#     s = json.loads(weibo_json)
#     print collection_fansWeibo.update({"fans_id":"789"}, {"$push":{"weibos": {"$each": s["statuses"]}}}, True)
#     # print s["statuses"][0]
# except Exception :
#     print "error"
#
# for fan in collection_newfans.find({}):
#     # if "work" in fan:
#         print fan["uid"]