from pydantic import BaseModel


class Corpus(BaseModel):
    text: str
