# encoding=utf-8
from pymongo import MongoClient
import json
import os

client = MongoClient('localhost', 27017)
db = client['test']
collection = db['fans']  # newfans

all_V = ["A1", "A2", "B1", "B2", "C1", "C2"]
all_folder = ["user", "info", "weibo"]

readinfo_error = 0
readweibo_error = 0

# 将user文件夹下的用户个人信息存入数据库
def read_user(dav):
    path = "/run/media/zice/DM/userProfile/"+dav+"user/"
    file_list = os.listdir(path)
    for info_file in file_list:
        f = open(path+info_file)
        response = f.read()
        oktext = response.replace('{{', '[{').replace('}}}', '}]}')
        s = json.loads(oktext)
        user = s["user"]
        a_fan = {
            "daV": dav,
            "uid": str(user["id"]),
            "name": user["name"],
            "location": user["location"],
            "gender": user["gender"],
            "followers_count": user["followers_count"],
            "friends_count": user["friends_count"],
            "statuses_count": user["statuses_count"],
            "credit_score": user["credit_score"],
            "tags": s["tags"],
            # 加入认证信息 待更新数据库
            "verified": user["verified"],
            "verified_type": user["verified_type"],

        }

        collection.insert(a_fan)

# 将info文件夹下的用户个人信息存入数据库
def read_info(dav):
    error = 0
    path = "/run/media/zice/DM/userProfile/"+dav+"info/"
    file_list = os.listdir(path)
    for info_file in file_list:
        f = open(path+info_file)
        response = f.read()
        try:
            s = json.loads(response)
        except Exception:
            error += 1
        # 工作
        if "work" in s:
            collection.update({"uid":s["id"]}, {"$set": {"work": s["work"]}})
        # 教育 要补读入数据库中
        if "education" in s:
            collection.update({"uid":s["id"]}, {"$set": {"education": s["education"]}})
    return error


# 将weibo文件夹下的用户weibo存入数据库
def read_weibo(dav):
    error = 0
    path = "/run/media/zice/DM/userProfile/"+dav+"weibo/"
    file_list = os.listdir(path)
    for info_file in file_list:
        f = open(path+info_file)
        # print info_file.split(".")[0]
        weibo_json = f.readlines()
        weibolist = []
        for line in weibo_json:
            try:
                s = json.loads(line)
                # print collection_fanWeibo.update({"uid": info_file.split(".")[0]}, {"$push": {"weibos": {"$each": s["statuses"]}}}, True)
                weibolist.append(s["statuses"])
            except Exception :
                error += 1
        collection.update({"uid": info_file.split(".")[0]}, {"$push": {"weibos": {"$each": s["statuses"]}}}, True)
    return error


def add_verified_from_user(dav):
    path = "/run/media/zice/DM/userProfile/"+dav+"user/"
    file_list = os.listdir(path)
    for info_file in file_list:
        f = open(path+info_file)
        response = f.read()
        oktext = response.replace('{{', '[{').replace('}}}', '}]}')
        s = json.loads(oktext)
        user = s["user"]
        # print user["verified_type"]
        collection.update({"uid":user["id"]}, {"$set": {"verified":user["verified"], "verified_type": user["verified_type"]}},True)

def add_edu_from_info(dav, error=readinfo_error):
    path = "/run/media/zice/DM/userProfile/"+dav+"info/"
    file_list = os.listdir(path)
    for info_file in file_list:
        f = open(path+info_file)
        response = f.read()
        try:
            s = json.loads(response)
        except Exception:
            error += 1
        # 教育 要补读入数据库中
        if "education" in s:
            collection.update({"uid": s["id"]}, {"$set": {"education": s["education"]}})

for v in all_V:
    print v
    # add_verified_from_user(v)
    print "user---"
    read_user(v)
    print "info---"
    readinfo_error += read_info(v)
    print "weibo---"
    readweibo_error += read_weibo(v)
    # print "--------------"
    # add_edu_from_info(v)
print "readinfo_error"
print readinfo_error
print "readweibo_erro"
print readweibo_error



