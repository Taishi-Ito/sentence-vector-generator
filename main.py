from fastapi import FastAPI, status
from pydantic import BaseModel, Field
import sentence_vector_generator.generator as generator
from fastapi.responses import JSONResponse

class Sentence(BaseModel):
    text: str = Field(min_length=1)

app = FastAPI()

@app.post("/generate")
async def generate(sentence: Sentence):
    try:
        vector_json = generator.generate_vector(sentence.text)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(e)})
    else:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"encoded_text": vector_json})
