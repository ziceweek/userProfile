# coding:utf-8
import bs4
from bs4 import BeautifulSoup
# from urllib import urlopen, urlencode
import urllib
import jieba
import jieba.posseg as pseg

from gensim import corpora, models, similarities


def token(sentence):
    words = pseg.cut(sentence)
    words_noun = []
    for w in words:
        if len(w.word) < 2:
            continue
        if w.flag[0:1] == 'n':
            words_noun.append(w.word)
    return words_noun

url = 'http://cloudtranslation.cc/cgi-bin/qq.cgi'
data = {
    'kw': '',
    'subcorp': 'xinhua',
}

# input: 一个词
# return: set类型的词集
def extend(word):
    data['kw'] = word.encode('utf8')
    final_url = url + '?' + urllib.urlencode(data)
    result = urllib.urlopen(final_url)

    content = result.read()
    soup = BeautifulSoup(content, from_encoding='utf-8')
    sentences = soup.find_all(name='td', attrs={"align": "left", "width": "50%"})
    words = set()

    for sentence in sentences:
        # words.append(list(jieba.cut(doc)))
        # words.append(token(sentence.get_text()))
        words = words.union(set(token(sentence.get_text())))
    return words

# example
# for w in extend('大熊猫'):
#        print w