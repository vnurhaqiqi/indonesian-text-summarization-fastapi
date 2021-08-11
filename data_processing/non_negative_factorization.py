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
        nmf_model = NMF(n_components=self.r, init='nndsvdar', solver='mu', beta_loss='frobenius', tol=0.1,
                        random_state=1)
        self.W = nmf_model.fit_transform(self.A)
        self.H = nmf_model.components_
        self.frobenius_norm = nmf_model.reconstruction_err_
        self.iter = nmf_model.n_iter_
        self.WH = self.W.dot(self.H)

    def display_summary(self):
        self.data = []
        self.index_data = []

        for topic_index, topic in enumerate(self.H):
            self.data.append([self.features_names[i] for i in topic.argsort()[:-self.num_top_words - 1:-1]])

            top_doc_indices = np.argsort(self.W[:, topic_index])[::-1][0:self.num_top_documents]
            self.index_data.append(top_doc_indices)

        summary_list = []
        for index in self.index_data[0]:
            summary_list.append(self.corpus[index])

        self.summary = summary_list

        data = {
            'top_words': self.data[0],
            'summary_result': self.summary
        }

        return data
