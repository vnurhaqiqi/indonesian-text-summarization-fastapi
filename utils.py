from response import *
from data_processing.text_preprocessing import *

response_obj = ResponseData()


def test():
    response_obj.set_status(200)
    response_obj.set_content("Hello World")

    return response_obj.get_response()


def summarizing_text(corpus):
    if not corpus:
        response_obj.set_status(400)
        response_obj.set_content("payload tidak boleh kosong.")

        return response_obj.get_response()

    preprocessing = corpus_preprocessing(corpus)

    response_obj.set_status(200)
    response_obj.set_content(preprocessing)

    return response_obj.get_response()