__author__ = 'zice'

from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
import datetime
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


def hello(request, name):
    return HttpResponse("hello "+name)


def show_date(request):
    now = datetime.datetime.now()
    html = "<html><body>it is now %s. </body></html>" % now
    return HttpResponse(html)


# use template to show html
def current_datetime2(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

# use more nice method to work
from django.shortcuts import render_to_response


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})

from django.db import connection


def check_test(request):
    cursor = connection.cursor()
    cursor.execute("select name from t1 limit 1,10")
    name = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return HttpResponse(name)


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def anlayis_dav(request):
    return render_to_response('explorV.html')


def anlayis_One(request):
    return render_to_response('explorOne.html')


def index(request):
    return render_to_response('index.html')