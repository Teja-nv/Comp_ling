import collections
import math

def tfidf(corpus):

        def tf(text):
                tf_text = collections.Counter(text)
        
                for i in tf_text:
        
                    tf_text[i] = tf_text[i]/float(len(text))
        
                return tf_text
        
        def idf(word, corpus):
        
                return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))
        
        documents_list = []
        
        for text in corpus:
        
                tf_idf_dictionary = {}
                
                computed_tf = tf(text)
                
                for word in computed_tf:
                
                        tf_idf_dictionary[word] = computed_tf[word] * idf(word, corpus)
                
                documents_list.append(tf_idf_dictionary)
                
        return documents_list        




corpus=[]
with open("Ot_Chego_zavisit_obschpol_poved.txt", 'r') as myself:
        for word in myself.read().split():
                corpus.append (word)



print (tfidf(corpus))



