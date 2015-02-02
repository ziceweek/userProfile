__author__ = 'zice'
from weibo import APIClient
import json

APP_KEY = '2038546250'
APP_SECRET = '24bb05a6fb21eadf36713d75f2fe2b77'
CALLBACK_URL = 'http://www.example.com/callback'


client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

access_token = '2.00aT9J3COAXxNCe7c300a699ZtkZjC'
expires_in = 1575207918
client.set_access_token(access_token, expires_in)

s = client.statuses.user_timeline.get(uid=1903209173)
# s = client.statuses.public_timeline.get()
f = open('we.txt', 'w')
f.write(repr(s))
