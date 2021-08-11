from main import app
from schemas import *
from utils import *


@app.get('/')
async def index():
    data = test()

    return data


@app.post('/api/v1/summarize-text')
async def summarize_text(payload: Corpus):
    corpus = payload.text
    num_words = payload.num_words
    num_sentences = payload.num_sentences
    text_tokenizing = sentence_tokenizing(corpus)
    text_preprocessing = preprocessing_data(text_tokenizing)
    text_summarizing = summarizing_data(text_preprocessing, text_tokenizing, num_words, num_sentences)

    return text_summarizing
