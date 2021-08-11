import nltk, re
import pandas as pd
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


def sentence_tokenizing(corpus):
    sentences_tokenize = sent_tokenize(corpus.lower())

    return sentences_tokenize


def corpus_preprocessing(sentences_tokenize):
    # nltk.download('punkt')
    # nltk.download('stopwords')

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

    return stemming_words


def weighting(stemming):
    vectorizer = CountVectorizer()

    words_freq = vectorizer.fit_transform(stemming)
    feature_names = vectorizer.get_feature_names()

    words_freq_df = pd.DataFrame(words_freq.todense(), columns=feature_names)

    data = {
        'm': len(words_freq_df.columns),
        'n': len(words_freq_df.index),
        'A': words_freq,
        'word_freq_matrix': words_freq_df,
        'feature_names': feature_names,
    }

    return data
