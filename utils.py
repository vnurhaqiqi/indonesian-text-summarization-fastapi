from response import *
from data_processing.text_preprocessing import *
from data_processing.non_negative_factorization import NonNegativeFactorization

response_obj = ResponseData()


def test():
    response_obj.set_status(200)
    response_obj.set_content("Peringkas Teks Bahasa Indonesia")

    return response_obj.get_response()


def preprocessing_data(corpus):
    if not corpus:
        response_obj.set_status(400)
        response_obj.set_content("payload tidak boleh kosong.")

        return response_obj.get_response()

    preprocessing = corpus_preprocessing(corpus)
    term_weighting = weighting(preprocessing)

    return term_weighting


def summarizing_data(pre_processing_data, sentence_tokenize, num_words, num_sentences):
    m, n = pre_processing_data['m'], pre_processing_data['n']
    feature_names = pre_processing_data['feature_names']
    A = pre_processing_data['A']
    sentences = sentence_tokenize

    r = False
    if m < n:
        r = m
    elif m > n:
        r = n
    elif m == n:
        r = m

    num_top_words = num_words if num_words else 5
    num_top_documents = num_sentences if num_sentences else 5

    nmf = NonNegativeFactorization(A=A, r=r, feature_names=feature_names, corpus=sentence_tokenize,
                                   num_top_words=num_top_words, num_top_documents=num_top_documents)
    decomposition = nmf.decomposition()
    summarize = nmf.display_summary()

    response_obj.set_status(200)
    response_obj.set_content(summarize)

    return response_obj.get_response()
