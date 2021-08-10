import nltk, re
import pandas as pd
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


def corpus_preprocessing(corpus):
    nltk.download('punkt')
    nltk.download('stopwords')

    sentences_tokenize = sent_tokenize(corpus.lower())

    remove_char = []
    for sentence in sentences_tokenize:
        remove_char.append(re.sub(r'-(?:(?<!\b[0-9]{4}-)|(?![0-9]{2}(?:[0-9]{2})?\b))', ' ', sentence))

    removetable = str.maketrans('', '', '@#%()[]{}.,!?><:;*&^+=_`~$"|/')
    clean_sentences = [sentence.translate(removetable) for sentence in remove_char]

    stopwords_indonesia = set(stopwords.words('indonesian'))
    sentences_stopwords = []

    for cl in clean_sentences:
        sentences_stopwords.append(' '.join(w for w in nltk.word_tokenize(cl) if w.lower() not in stopwords_indonesia))

    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    stemming_words = []
    for ss in sentences_stopwords:
        stemming_words.append(stemmer.stem(ss))

    # TODO: add term weighting

    return stemming_words
