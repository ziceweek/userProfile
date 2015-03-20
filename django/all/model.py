# coding:utf-8
import DBopr
import json
from pymongo import MongoClient
import string
import datetime,time
import re
import chardet

class Fan(object):

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
        if "weibos" in fan_info_json:
            self.weibos = fan_info_json["weibos"]
        else:
            self.weibos = []

        self.all_client = {}
        self.client = ""
        self.frequece = 0
        self.weibo_log = {}

        self.reposts_count = 0
        self.comments_count = 0
        self.attitudes_count = 0

        self.topic_words = []
    # 统计微博转发评论点赞数
    def count_weibos(self):
        rc = 0
        cc = 0
        ac = 0
        for weibo in self.weibos:
            # print int(weibo["reposts_count"])
            rc += int(weibo["reposts_count"])
            cc += int(weibo["comments_count"])
            ac += int(weibo["attitudes_count"])
        self.reposts_count = rc
        self.comments_count = cc
        self.attitudes_count = ac

    # 统计客户端类型
    def count_client(self):
        pat = re.compile(r'<.*?>')
        for weibo in self.weibos:
            result = pat.sub("", weibo["source"]).replace(".","")

            if result in self.all_client:

                self.all_client[result] += 1
            else:
                self.all_client[result] = 1

        # 取最常用的客户端作为代表
        m = 0
        for c in self.all_client:
            # print c
            if self.all_client[c] > m:
                self.client = c
                m = self.all_client[c]

        # # 打印所有
        # for u in self.all_client:
        #     print u[0]
        #     print u[1]
        #     print "----"

    # 统计发博时间和频率
    # return：一个词典，键是日期，值是当天微博条数
    def count_twee_time(self):

        self.weibo_log = {}
        pat = re.compile(r'\+[0-9]{4}')

        for weibo in self.weibos:
            datetime_str = weibo["created_at"]
            result = pat.search(datetime_str)
            f = datetime_str.replace(datetime_str[result.start(0)-1:result.end(0)],"")
            d = datetime.datetime.strptime(f, "%a %b %d %H:%M:%S %Y")
            if d.date() in self.weibo_log:
                self.weibo_log[str(d.date())] += 1
            else:
                self.weibo_log[str(d.date())] = 1

        # 发博频率
        try:
            self.frequece = len(self.weibos)/len(self.weibo_log)
        except(ZeroDivisionError,TypeError):
            self.frequece = 0

    # 将该对象更新到数据库
    def update(self):
        DBopr.update_fan_model_to_db(self)

    def analysis(self):

        self.count_weibos()
        self.count_client()
        self.count_twee_time()
        self.update()

class DaV(object):

    def __init__(self, id="A1"):
        self.id = id

        self.gender = {"m":0,"f":0}
        self.active = {}
        self.client = {}
        self.region = {}
        self.education = {"大学": 0, "中学": 0, "中专技校":0}
        self.tags = {}
        self.verified = {}
        self.provinces = {}
        self.fans_count = 0


    def statistics_fan(self):
        fans = DBopr.get_fan_by_dav(self.id)

        for fan in fans:
            print fan["name"]

            # 统计总粉丝数目
            self.fans_count += 1
            # 统计性别
            if "gender" in fan:
                self.gender[fan["gender"]] += 1

            # 统计位置,按省份
            province = fan["location"].split(" ")[0]
            if province in self.provinces:
                self.provinces[province] += 1
            else:
                self.provinces[province] = 1

            # 教育，分三个，没有的分为其他或未知
            if "education" in fan:
                print fan["education"].replace(" ","")
                if not fan["education"].find(u"大学") == -1:
                    self.education["大学"] += 1
                elif not fan["education"].find(u"中学") == -1:
                    self.education["中学"] += 1
                elif not fan["education"].find(u"中专技校") == -1:
                    self.education["中专技校"] += 1

            # print fan
            # 认证类型，需要再弄一个对照表
            if str(fan["verified_type"]) in self.verified:
                self.verified[str(fan["verified_type"])] += 1
            else:
                self.verified[str(fan["verified_type"])] = 1

            # 统计客户端类型
            if "client" in fan:
                if fan["client"] in self.client:
                    self.client[fan["client"]] += 1
                else:
                    self.client[fan["client"]] = 1

    def update_to_db(self):
        print "to db done"
        DBopr.update_dav_model_to_db(self)
