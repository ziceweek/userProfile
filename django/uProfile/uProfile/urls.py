from django.conf.urls import patterns, include, url
from django.contrib import admin
from view import *

urlpatterns = patterns('',
                       ('^hello/(.+)/$', hello),
                       ('^datetime/$', show_date),
                       ('^current/$', current_datetime),
                       ('^test/$', check_test),
                       ('^meta/$', display_meta),
                       ('^search-form/$', search_form),
                       ('^search/$', search),
                       )
