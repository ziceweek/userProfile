# coding:utf-8
import DBopr
import json
from pymongo import MongoClient
import string
import datetime,time
import re


class Fan(object):
    reposts_count = 0
    comments_count = 0
    attitudes_count = 0

    def __init__(self, fan_uid="1008912684"):
        fan_info_json = DBopr.get_fan_by_uid(fan_uid)
        # fan_info_json = json.loads(fan_json)
        self.uid = fan_uid
        self.name = fan_info_json["name"]
        self.location = fan_info_json["location"]
        self.gender = fan_info_json["gender"]
        self.followers_count = fan_info_json["followers_count"]
        self.friends_count = fan_info_json["friends_count"],
        self.statuses_count = fan_info_json["statuses_count"],
        self.credit_score = fan_info_json["credit_score"],
        # selfTags = fan_info_json["tags"]
        self.tags = fan_info_json["tags"]
        self.weibos = fan_info_json["weibos"]

    def count_weibos(self):
        # 统计微博转发评论点赞数
        rc = 0
        cc = 0
        ac = 0
        for weibo in self.weibos:
            # print int(weibo["reposts_count"])
            rc += int(weibo["reposts_count"])
            cc += int(weibo["comments_count"])
            ac += int(weibo["attitudes_count"])
        print rc
        print cc
        print ac

    def count_client(self):
        # 统计客户端类型
        u_client = {}
        pat = re.compile(r'<.*?>')
        for weibo in self.weibos:
            result = pat.sub("",weibo["source"])
            if result in u_client:
                u_client[result] += 1
            else:
                u_client[result] = 1
        for u in u_client:
            print u
            print u_client[u]
            print "----"

    def count_twee_time(self):

        twe_date = {}
        pat = re.compile(r'\+[0-9]{4}')

        for weibo in self.weibos:
            datetime_str = weibo["created_at"]
            result = pat.search(datetime_str)
            f = datetime_str.replace(datetime_str[result.start(0)-1:result.end(0)],"")
            d = datetime.datetime.strptime(f, "%a %b %d %H:%M:%S %Y")
            if d.date() in twe_date:
                twe_date[d.date()] += 1
            else:
                twe_date[d.date()] = 1
        date_count = len(self.weibos)/len(twe_date)
        print date_count
        return twe_date
