import collections
import math


def tf(corpus):
        tf_corpus = collections.Counter(corpus)

        for i in tf_corpus:

            tf_corpus[i] = tf_corpus[i]/float(len(corpus))

        return tf_corpus

def idf(word, corpus):

        return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))





corpus=[]
with open("Ot_Chego_zavisit_obschpol_poved.txt", 'r') as myself:
        for word in myself.read().split():
                corpus.append (word)


print (tf(corpus))
print (idf("люди",corpus))


