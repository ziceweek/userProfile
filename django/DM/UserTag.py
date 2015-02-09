# coding:utf-8
import bs4
from bs4 import BeautifulSoup
import jieba.posseg as pseg
from gensim import corpora, models, similarities

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

# 从文本中获取原始数据
# argus: 文本路径
# return: [],元素是每一条微博
def get_weiboList(filepath='sampleData.txt'):
    weibolist = []
    infile = open(filepath)
    for line in infile.readlines():
        soup = BeautifulSoup(line)
        ot = soup.originText
        t = soup.select('text')[0].text
        if ot is not None:
            o = ot.text
            t = t+' '+o
        weibolist.append(t)
    return weibolist


# lsi model:
# input: 产生的话题个数
# return: list，每个条目是表示一个话题的字符串
def get_lsi(num='20'):
    # 得到 文档-词 矩阵
    words = []
    for doc in get_weiboList('/home/zice/userProfile/django/sampleData.txt'):
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
def get_lda(num_topics='20'):
    # 得到 文档-词 矩阵
    words = []
    for doc in get_weiboList('/home/zice/userProfile/django/sampleData.txt'):
        # words.append(list(jieba.cut(doc))) # 取全部的词
        words.append(token(doc))  # 只取名词

    # 由 文档-词 矩阵，得到一个全文的词典
    id2word = corpora.Dictionary(words)

    # make a corpus
    corpus = [id2word.doc2bow(text) for text in words]

    # tf-idf transform
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    lda = models.LdaModel(corpus_tfidf, id2word, num_topics)
    ldaOut = lda.print_topics(num_topics)
    return ldaOut


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