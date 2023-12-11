from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from chatbot import generate_response
import asyncio

app = FastAPI()

class QueryItem(BaseModel):
    query: str

@app.post("/api/chat")
async def chat(item: QueryItem):
    user_query = item.query
    #calling chatbot to generate a response
    bot_response = generate_response(user_query)

    return {'response': bot_response}


