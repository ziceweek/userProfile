__author__ = 'zice'

from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.template.loader import get_template
import os
from weibo import APIClient
from django.shortcuts import render_to_response
import re

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

APP_KEY = '2038546250'
APP_SECRET = '24bb05a6fb21eadf36713d75f2fe2b77'
CALLBACK_URL = 'http://www.example.com/callback'

code = ''


def login(request):
    return render_to_response('login.html')


def get_code(URL):
    pat = re.compile(r'=.*')
    result = pat.search(URL)
    s = result.start(0)
    e = result.end(0)
    return URL[s+1:e]


def goto_get_authorize_page(request):
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    code = get_code(url)
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    r = client.request_access_token(code)
    access_token = r.access_token  # token given by sina like 'abc123xyz456'
    expires_in = r.expires_in  # token avaivable time
    client.set_access_token(access_token, expires_in)
    return HttpResponseRedirect('http://localhost:8000/welcome')
    # return HttpResponseRedirect(url)



def welcome(request):
    content = client.statuses.user_timeline.get()
    return render_to_response(content)

