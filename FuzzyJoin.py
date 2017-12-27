import pandas as pd
from sklearn.cluster import KMeans
import gensim
from nltk import word_tokenize
from fuzzywuzzy import fuzz
from itertools import chain

def FuzzyJoin(tbl1, tbl2, by, stop_words = []):

    centers = tbl1[by[0]]
    fkeys = tbl2[by[-1]]

    ############Testing for the Practie Titles##########
    centers_l = [[w.lower() for w in word_tokenize(center) if w not in stop_words]
                for center in list(centers)]
    centers_set = set(chain.from_iterable(centers_l)) + stop_words
    center_vectors = pd.DataFrame(np.zeros([len(centers_l),len(centers_set)]),
                                columns = centers_set)

    for i,center in enumerate(centers_l):
        for w in center:
            center_vectors.loc[center_vectors.index[i], w] += 1
    
    fkeys_l = [[w.lower() for w in word_tokenize(fkey) if w not in centers_set]
               for fkey in list(fkeys)]
    fkey_vectors = pd.DataFrame(np.zeros([len(fkeys_l),len(centers_set)]),
                                columns = centers_set)

    for i,fkey in enumerate(fkeys_l):
        for w in fkey:
            fkey_vectors.iloc[fkey_vectors.index[i], w] +=1

    cent_m = np.array(center_vectors)
    fkey_m = np.array(fkey_vectors)
    crossed = np.matmul(cent_m, fkey_m.transpose())

    maxi = np.argmax(crossed,axis = 0)
    tbl2[by[0]] = tbl1.iloc[list(maxi),by[0]]

    return(pd.merge(tbl1,tbl2, how='inner', on=by[0]))

    
    ##Now this is definitely a baseline method. Needs Improving:
    ##1. How to quantify the flexibility. Should "The Middlebury Clinic" match with
    ##  "The Middlebury Hospital"? I think in that case its up to you to supply the correct
    ##  stop_words. You want to distinguish Clinic from Hospital
