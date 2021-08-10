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
    data = summarizing_text(corpus)

    return data
