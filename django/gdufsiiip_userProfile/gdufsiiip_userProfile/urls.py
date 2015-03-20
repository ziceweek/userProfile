from django.conf.urls import patterns, include, url
from django.contrib import admin
from views.login import *
urlpatterns = patterns(
    (r'^admin/', include(admin.site.urls)),
    # (r'^welcome/', welcome),
    (r'^login/', login),
    (r'^goto_get_authorize_page/', goto_get_authorize_page),
)
