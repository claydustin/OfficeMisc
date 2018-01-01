import pandas as pd
from sklearn.cluster import KMeans
import gensim
from nltk import word_tokenize
from fuzzywuzzy import fuzz
from itertools import chain

def WordDocMatrix(documents, stop_words = []):

    #Leave this function to be accompanied with np.matmul and np.argmax
    #to find documents with the most words in common

    docs = [[w.lower() for w in word_tokenize(doc) if w not in stop_words] for doc in documents]

    words_set = set(chain.from_iterable(docs))
    wordDoc = pd.DataFrame(np.zeros([len(words_set), len(words_set)]), columns = words_set)

    for i,words in enumerate(docs):
        for w in words:
            wordDoc.loc[center_vectors.index[i], w] += 1
    return wordDoc

