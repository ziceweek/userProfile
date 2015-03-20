from django.conf.urls import patterns, include, url
import django.contrib.staticfiles
from django.contrib import admin
from django.conf import settings
from view import *
import settings
from new_view import *

root_path = os.path.dirname(globals()["__file__"])

urlpatterns = patterns('',
                       url( r'^static/(?P<path>.*)$', 'django.views.static.serve',
                       { 'document_root':settings.STATICFILES_DIRS }),
                       ('^hello/(.+)/$', hello),
                       ('^datetime/$', show_date),
                       ('^current/$', current_datetime),
                       ('^test/$', check_test),
                       ('^meta/$', display_meta),
                       ('^search-form/$', search_form),
                       ('^search/$', search),
                       ('^dav/$', anlayis_dav),
                       ('^index/$', index),
                       ('^one/$', anlayis_One),

                       )

