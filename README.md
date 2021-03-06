# Indonesian Text Summarization Using FastAPI

This is REST-API for Indonesian Text Summarization using Non-Negative Matrix Factorization for the algorithm to summarize documents and FastAPI for the framework.

## Quick Start

```sh
$ create virtual environment
$ source env/bin/activate
$ install all depencies pip install -r requirements.txt
```

## Run

```sh
$ run by uvicorn: uvicorn main:app --reload
$ run the app: python main.py
$ or you can use sh: run.sh
```

## REST-API Documentations

### Get Summarization
#### Url path & Method

`POST /api/v1/summarize-text`

    http://0.0.0.0:8000/api/v1/summarize-text

#### Request Body

    application/json: {
      "text": "string",
      "num_words": 0,
      "num_sentences": 0
    }
    
    - text [string]: text or corpus to be summarized
    - num_words [int]: numbers of top words in text or corpus
    - num_sentences: numbers of top sentences in text or corpus

#### Response

`status 200`

    HTTP/1.1 200 OK
    Status: 200 OK
    Connection: close
    Content-Type: application/json

    {
        'content': {
            'top_words': [],
            'summary_result': []
        },
        'status_code': 200,
        'message': "Success"
    }

`status 400`

    HTTP/1.1 400 Bad Request
    Status: 400 Bad Request
    Connection: close
    Content-Type: application/json

    {
        'content': "payload tidak boleh kosong",
        'status_code': 400,
        'message': "Bad Request"
    }
