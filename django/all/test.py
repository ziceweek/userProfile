# coding:utf-8
__author__ = 'zice'
from model import Fan,DaV
from pymongo import MongoClient
import datetime
import re
from Tag import get_fan_tag_from_weibo_text

client = MongoClient('localhost', 27017)
db = client['test']
collection_daV = db['fans']


all_V = ["A1", "A2", "B1", "B2", "C1", "C2"]

# 处理大V的粉丝们
# for dav in all_V:
#     fans = collection_daV.find({"daV": dav})
#     print dav
#     for fan in fans:
#         f = Fan(fan["uid"])
#         print "processing"+f.name
#         f.topic_word = get_fan_tag_from_weibo_text(f)
#         f.analysis()


for d in all_V:
    print d
    dav = DaV(d)
    dav.statistics_fan()
    dav.update_to_db()
