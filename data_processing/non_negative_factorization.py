from sklearn.decomposition import NMF
from nltk.tokenize import sent_tokenize
import numpy as np


class NonNegativeFactorization():
    def __init__(self, A, r, feature_names, num_top_words, num_top_documents, corpus):
        self.A = A
        self.r = r
        self.features_names = feature_names
        self.corpus = corpus
        self.num_top_words = num_top_words
        self.num_top_documents = num_top_documents

    def decomposition(self):
        print("==res==")
        print(self)

        err
