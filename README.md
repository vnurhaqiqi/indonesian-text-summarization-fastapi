# Indonesian Text Summarization Using FastAPI

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

