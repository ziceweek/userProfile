# encoding=utf-8
__author__ = 'zice'

from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['test']
collection = db['fans']

# 根据uid获取某一个粉丝
def get_fan_by_uid(fan_id):
    fan = collection.find_one({"uid":fan_id})
    return fan

# 获取某个大V的粉丝列表
def get_fan_by_dav(dav_id="A1"):
    fans = collection.find({"daV": dav_id})
    return fans

# 将会修改到的字段，或者新产生的字段更新到数据库中
def update_fan_model_to_db(fan):
    # debug
    # print "all_client:"
    # print fan.all_client
    # print "client:"
    # print fan.client
    # print "frequece:"
    # print fan.frequece
    # print "reposts_count:"
    # print fan.reposts_count
    # print "comments_count:"
    # print fan.comments_count
    # print "attitudes_count:"
    # print fan.attitudes_count
    # print "weibo_log:"
    # print fan.weibo_log
    # print "topic_words:"
    # print fan.topic_words
    collection.update({"uid": fan.uid},
                      {"$set": {
                          "all_client": fan.all_client,
                          "client": fan.client,
                          "frequece": fan.frequece,
                          "reposts_count": fan.reposts_count,
                          "comments_count": fan.comments_count,
                          "attitudes_count": fan.attitudes_count,
                          "weibo_log": fan.weibo_log,
                          "topic_words": fan.topic_words
                          }
                      }, True)


def update_dav_model_to_db(dav):
    collection.update({"uid": dav.id},
                      {"$set": {
                          "gender": dav.gender,
                          "client": dav.client,
                          "region": dav.region,
                          "education": dav.education,
                          "tags": dav.tags,
                          "verified": dav.verified,
                          "provinces": dav.provinces,
                          "fans_count":dav.fans_count
                          }
                      }, True)

# s = get_fan_by_uid("1136750677")
# print s["name"]

get_fan_by_dav()