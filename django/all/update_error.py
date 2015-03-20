# coding:utf-8
from model import Fan,DaV
from pymongo import MongoClient
from Tag import get_fan_tag_from_weibo_text


client = MongoClient('localhost', 27017)
db = client['test']
collection_daV = db['newfans']



# f = Fan("1008912684")
f = Fan("1058442313")
print "processing"+f.name
f.topic_word = get_fan_tag_from_weibo_text(f)
f.analysis()
