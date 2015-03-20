import json
import os
from pymongo import MongoClient



client = MongoClient('localhost', 27017)
db = client['test']
collection_newfans = db['newfans']

def read_info(dav):
    path = "/run/media/zice/DM/userProfile/"+dav+"info/"
    file_list = os.listdir(path)
    i = 0
    for info_file in file_list:
        f = open(path+info_file)
        response = f.read()
        try:
            s = json.loads(response)
        except Exception:
            i += 1

        if "work" in s:
            print collection_newfans.update({"uid":s["id"]}, {"$set": {"work": s["work"]}})
            for c in collection_newfans.find({"uid":s["id"]}):
                if "work" in c:
                    print c["work"]
            print "--------"



for dav in ["A1", "A2", "B1", "B2", "C1", "C2"]:
    read_info(dav)

for a in collection_newfans.find():
    if "work" in a:
        print a["work"]