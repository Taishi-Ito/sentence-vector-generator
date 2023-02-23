from fastapi import FastAPI
from pydantic import BaseModel
import sentence_vector_generator.generator as generator
from fastapi.responses import JSONResponse

class Sentence(BaseModel):
    text: str

app = FastAPI()

@app.post("/generate")
async def generate(sentence: Sentence):
    vector_json = generator.generate_vector(sentence.text)
    return JSONResponse(content={"encoded_text": vector_json})
