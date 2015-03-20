from pymongo import MongoClient
import json
import os
# client = MongoClient('localhost', 27017)
# db = client['test']
# collection_fans = db['fans']

for user in os.listdir("/run/media/zice/DM/userProfile/A1user/"):
    user
f = file("/run/media/zice/DM/userProfile/A1user/273429975.txt")
response = f.read()
oktext = response.replace('{{', '[{').replace('}}}', '}]}')

s = json.loads(oktext)
print s["tags"]

f.close()


# collection_fans.insert(s)
# collection_fans.insert(fan2)

# for fan in collection_fans.find():
    # print fan
