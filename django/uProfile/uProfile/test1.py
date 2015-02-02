__author__ = 'zice'


import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.template import Template, Context
t = Template("this is my name --{{ name }}")
c = Context({'name': 'zice'})

print t.render(c)
