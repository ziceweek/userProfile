#
# coding=utf-8
#
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
        if w.flag[0:1] == 'n':
            words_noun.append(w.word)
    return words_noun




url = 'http://cloudtranslation.cc/cgi-bin/qq.cgi'
data = {
    'kw': '肯德基',
    'subcorp': 'xinhua',
}
final_url = url + '?' + urllib.urlencode(data)
result = urllib.urlopen(final_url)

content = result.read()

print content

outfile = open('content.html', 'w')
outfile.write(content)
outfile.close()
soup = BeautifulSoup(content, from_encoding='utf-8')
weiboList = soup.find_all(name='td', attrs={"align": "left", "width": "50%"})
sentences = []
for w in weiboList:
    print w.get_text()
    sentences.append(w.get_text())

# cut the example into words
words = []
for doc in sentences:
    # words.append(list(jieba.cut(doc)))
    words.append(token(doc))
    # print words

# make a dict
dic = corpora.Dictionary(words)

# make a corpus
corpus = [dic.doc2bow(text) for text in words]

# tf-idf transform
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]


# lsi model:
lsi = models.LsiModel(corpus_tfidf,id2word=dic,num_topics=2)
lsiout = lsi.print_topics(2)
print lsiout[0]
print lsiout[1]

corpus_lsi = lsi[corpus_tfidf]
# for doc in corpus_lsi:
#     print doc

# lda model:
# lda = models.LdaModel(corpus_tfidf,id2word=dic,num_topics=2)
# ldaOut = lda.print_topics(2)
# print ldaOut[0]
# print ldaOut[1]
# corpus_lda = lda[corpus_tfidf]
# for doc in corpus_lda:
#     print doc

# input a word and check it's theme
index = similarities.MatrixSimilarity(lsi[corpus])
query = "薯条"
query_bow = dic.doc2bow(list(jieba.cut(query)))
query_lsi = lsi[query_bow]
print query_lsi

sims = index[query_lsi]
print list(enumerate(sims))
sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
print sort_sims