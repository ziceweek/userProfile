# coding:utf-8
__author__ = 'zice'
from UserTag import get_lsi, LSI
from topic import get_topic_words_in_str_1
from extend import extend


topics_str = get_lsi(10)
topics_dcit = []
for topic in topics_str:
    topics_dcit = get_topic_words_in_str_1(topic)

for u in topics_dcit:
    print u

