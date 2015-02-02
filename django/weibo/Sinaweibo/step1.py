__author__ = 'zice'

from weibo import APIClient
APP_KEY = '2038546250'
APP_SECRET = '24bb05a6fb21eadf36713d75f2fe2b77'
CALLBACK_URL = 'http://www.example.com/callback'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print url
# TODO: redirect to url