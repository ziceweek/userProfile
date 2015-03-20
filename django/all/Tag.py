# coding:utf-8
__author__ = 'zice'
from UserTag import get_lsi,get_lda, LSI
import re
from model import Fan

pat = re.compile(r'"(.*)"')
pat_lda = re.compile(r'\*')


def _get_topic_words_in_str_lsi(topic_str):
    dict_of_a_topic = []
    items = topic_str.split('+')
    for word in items:
        result = pat.search(word)
        dict_of_a_topic.append(result.group(1))
    return dict_of_a_topic


def _get_topic_words_in_str_lda(topic_str):
    dict_of_a_topic = []
    items = topic_str.split('+')
    for word in items:
        result = pat_lda.search(word)
        if result is not None:
            dict_of_a_topic.append(word[result.start(0)+1:])
    return dict_of_a_topic


def _get_weiboList(fan):
    weibolist = []
    for weibo in fan.weibos:
        content = weibo["text"] + " "
        if "retweeted_status" in weibo:
            content += weibo["retweeted_status"]["text"]
        weibolist.append(content)
    return weibolist


# input: 一个粉丝对象
# return: 一个主题词列表
# 使用lsi或者lda
def get_fan_tag_from_weibo_text(fan=Fan()):

    weibolist = _get_weiboList(fan)

    if len(weibolist) > 1:  # 多与1条微博才计算lda
        # topics_str = get_lsi(weibolist)
        topics_str = get_lda(weibolist)
        topics_dict = []
        for topic in topics_str:
            topics_dict.extend(_get_topic_words_in_str_lda(topic))
            # topics_dict = _get_topic_words_in_str_lsi(topic)
        return topics_dict
    else:
        return weibolist


# topics_dict = get_fan_tag_from_weibo_text()
# for u in topics_dict:
#     print u

# 计算一个粉丝列表中每个粉丝的主题词
# input: 一个元素为Fan类型的列表
# return: 一个词典，键为fan的uid，值是fan的主题词列表
def count_fanlist_tags(fan_list):
    fans_tag = {}
    for fan in fan_list:
        tags = get_fan_tag_from_weibo_text(fan)
        fans_tag[fan.uid]=tags
    return fans_tag

