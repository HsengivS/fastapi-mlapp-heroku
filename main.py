from typing import Text
from fastapi import FastAPI
from textblob import TextBlob

app = FastAPI()

@app.get("/")
def index():
    return "<h1>Welcome to hsengivs</h1>"

@app.get("/items/{text}")
async def read_item(text: str):
    wiki = TextBlob(text)
    return {"result":wiki.tags}
