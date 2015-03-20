__author__ = 'zice'
from model import Fan
import datetime
import re

fan = Fan()

print fan.name
print fan.location
print fan.tags

# fan.count_weibos()
# fan.count_client()
twe_date = fan.count_twee_time()
print len(twe_date)
for d in twe_date:
    print str(d)+" "+str(twe_date[d])
