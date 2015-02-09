# coding:utf-8
__author__ = 'zice'
from UserTag import get_lsi, LSI
from topic import get_topic_words_in_str
from extend import extend

outfile1 = open('first_topics.txt', 'w')
outfile2 = open('second_topics.txt', 'w')

topics_str = get_lsi(10)
topics_dcit = []
for topic in topics_str:
    topics_dcit.append(get_topic_words_in_str(topic))

for t in topics_dcit:
    outfile1.writelines('------------------topic--------\n')
    for w in t:
        t[w] = extend(w)
        outfile1.write(w.encode('utf8')+':')
        for tw in t[w]:
            outfile1.write(tw.encode('utf8')+' ')
        outfile1.writelines('---\n')
    outfile1.writelines('---\n')

new_topic = []
new_topic_dict = []
for t in topics_dcit:
    outfile2.writelines('------------------topic--------\n')
    new_topic_str = LSI(t.values(), 1)[0]
    for nw in get_topic_words_in_str(new_topic_str).keys():
        outfile2.write(nw.encode('utf8')+' ')
    outfile2.writelines('---\n')
