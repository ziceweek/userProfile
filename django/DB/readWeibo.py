import json
import os
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['test']
collection_fanWeibo = db['fanWeibo']

i = 0
error_count = 0


def read_weibo(dav):
    path = "/run/media/zice/DM/userProfile/"+dav+"weibo/"
    file_list = os.listdir(path)
    i = 0
    error_count = 0
    for info_file in file_list:
        f = open(path+info_file)
        print info_file.split(".")[0]
        weibo_json = f.readlines()
        weibolist = []
        for line in weibo_json:
            try:
                s = json.loads(line)
                # print collection_fanWeibo.update({"uid": info_file.split(".")[0]}, {"$push": {"weibos": {"$each": s["statuses"]}}}, True)
                weibolist.append(s["statuses"])
                i += 1
            except Exception :
                error_count += 1
                print "error"
        print collection_fanWeibo.update({"uid": info_file.split(".")[0]}, {"$push": {"weibos": {"$each": s["statuses"]}}}, True)
        print "--------"


for dav in ["A2"]:
    print dav
    read_weibo(dav)

print "success:"
print i
print "fail:"
print error_count

# for a in collection_newfans.find():
#     if "work" in a:
#         print a["work"]