import spacy
from fastapi import FastAPI

nlp = spacy.load("en_core_web_lg")

app = FastAPI()

@app.get("/")
def index():
    return "<h1>Say hello to hsengivs</h1>"

@app.post("/ner")
async def read_item(text: str):
    try:
        doc = nlp(text)
        result = doc.to_json()
        return {"result":result}
    except Exception as e:
        return {"result": str(e)}
