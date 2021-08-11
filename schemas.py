from pydantic import BaseModel
from typing import Optional


class Corpus(BaseModel):
    text: str
    num_words: Optional[int] = None
    num_sentences: Optional[int] = None
