# coding:utf-8
import bs4
from bs4 import BeautifulSoup
import jieba.posseg as pseg
from gensim import corpora, models, similarities
from model import Fan

# 只取名词
# argus: 要分词的目标字符串
# return: []
def token(sentence):
    words = pseg.cut(sentence)
    words_noun = []
    for w in words:
        if w.flag[0:1] == 'n':
            words_noun.append(w.word)
    return words_noun

# lsi model:
# input: 产生的话题个数
# return: list，每个条目是表示一个话题的字符串
def get_lsi(weiboList,num='10'):
    # 得到 文档-词 矩阵
    words = []
    for doc in weiboList:
        # words.append(list(jieba.cut(doc))) # 取全部的词
        words.append(token(doc))  # 只取名词

    # 由 文档-词 矩阵，得到一个全文的词典
    dic = corpora.Dictionary(words)
    # make a corpus
    corpus = [dic.doc2bow(text) for text in words]
    # tf-idf transform
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    lsi = models.LsiModel(corpus_tfidf, id2word=dic, num_topics=num)
    lsiout = lsi.print_topics(num)
    return lsiout

# lda model:
def get_lda(weiboList,num=20):
    # 得到 文档-词 矩阵
    words = []
    for doc in weiboList:
        # words.append(list(jieba.cut(doc))) # 取全部的词
        words.append(token(doc))  # 只取名词

    # 由 文档-词 矩阵，得到一个全文的词典
    dic = corpora.Dictionary(words)

    # make a corpus
    corpus = [dic.doc2bow(text) for text in words]

    # tf-idf transform
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    if len(dic) > 0:
        lda = models.LdaModel(corpus_tfidf, id2word=dic, num_topics=num)
        ldaOut = lda.print_topics(num)
        return ldaOut
    else:
        return ""


# Example
# for k in get_lsi():
#    print k


# lsi model:
# input: words 文档-词 矩阵, words 产生的话题个数
# return: list，每个条目是表示一个话题的字符串
def LSI(words, num='20'):

    # 由 文档-词 矩阵，得到一个全文的词典
    dic = corpora.Dictionary(words)
    # make a corpus
    corpus = [dic.doc2bow(text) for text in words]
    # tf-idf transform
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    lsi = models.LsiModel(corpus_tfidf, id2word=dic, num_topics=num)
    lsiout = lsi.print_topics(num)
    return lsiout