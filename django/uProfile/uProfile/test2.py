__author__ = 'zice'

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# from koob.models import Publisher
# p1 = Publisher(name='OReilly', address='2855 Telegraph Avenue',city='Berkeley', state_province='CA', country='U.S.A.', website='http://www.apress.com/')
#
# p1.save()
#
# publisher_list = Publisher.objects.all()
# print publisher_list

from test.models import t1
p1 = t1(id=007, name='OReilly')

p1.save()

publisher_list = t1.objects.all()
print publisher_list