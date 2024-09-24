from fastapi import FastAPI
import os
from pydantic import BaseModel
from chat import get_llm_response, vectordb


app = FastAPI()
is_prod = os.environ.get("IS_HEROKU", None)


class RequestAsk(BaseModel):
    question: str = "What is UV-C ?"
    model: str = "gpt-4o-mini"
    temp: float = 0.1
    k: int = 10
    overwrite: bool = False
    source: str = "api"
    seed: str = ""


@app.post("/ask/")
async def ask(itemR: RequestAsk):
    a, d = get_llm_response(
        itemR.question, vectordb, temperature=itemR.temp,
        k=itemR.k, seed=itemR.seed, ow = itemR.overwrite
    )
    return {"answer": a, "refs": d}


@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "is_prod": is_prod,
        "TestSecret": os.environ.get("CACHE"),
    }
