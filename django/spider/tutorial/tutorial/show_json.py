__author__ = 'zice'

# coding:utf-8
import json

f = file("explore.json")
response = f.read()
s = json.loads(response)
for i in s:
    print i["category"], i["name"]
f.close