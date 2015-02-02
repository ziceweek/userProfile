__author__ = 'zice'
from gensim import corpora, models, similarities

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

# lda model:
lda = models.LdaModel(corpus_tfidf,id2word=dic,num_topics=2)
ldaOut = lda.print_topics(2)
print ldaOut[0]
print ldaOut[1]
corpus_lda = lda[corpus_tfidf]
for doc in corpus_lda:
    print doc