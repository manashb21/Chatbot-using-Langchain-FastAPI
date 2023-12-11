import asyncio
from typing import AsyncIterable, Awaitable

import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from pydantic import BaseModel

app = FastAPI()    

llm = CTransformers(model = "model", 
                    model_file = "llama-2-7b-chat.Q4_K_M.gguf",
                    config = {'max_new_tokens' : 1024,
                              'repetition_penalty': 1.1,
                              'temperature': 0.8,
                            'context_length' : 8192},
                    streaming = True,
                    callbacks = [AsyncIteratorCallbackHandler()])
template = """
    [INST] <<SYS>>
    You are a helpful, respectful and honest assistant who answers questions about technology, coding, and IT. 
    Your answers are to the point and always brief. 
    You donot provide information or answer about socio-cultural, racial, political and any sensitive topic and incase 
    those topics are asked, just say you don't know and stop explaining. 

    If you don't know answer about something, say you don't know. Donot create your own answer.
    <</SYS>>
    {text}
    [/INST]
    """

prompt = PromptTemplate(template=template, input_variables=["text"])

llm_chain = LLMChain(prompt=prompt, llm=llm)


async def send_message(message: str) -> AsyncIterable[str]:
    callback = llm.callbacks[0]

    async def wrap_done(fn: Awaitable, event: asyncio.Event):
        """Wrap an awaitable with a event to signal when it's done or an exception is raised."""
        try:
            await fn
        except Exception as e:
            # TODO: handle exception
            print(f"Caught exception: {e}")
        finally:
            # Signal the aiter to stop.
            event.set()

    # Begin a task that runs in the background.
    task = asyncio.create_task(wrap_done(llm_chain.arun(message),callback.done),)

    async for token in callback.aiter():
        # Use server-sent-events to stream the response
        yield f"{token}\n\n"

    await task


class StreamRequest(BaseModel):
    """Request body for streaming."""
    message: str


@app.post("/stream")
def stream(body: StreamRequest):
    return StreamingResponse(send_message(body.message), media_type="text/event-stream")


# if __name__ == "__main__":
#     uvicorn.run(host="0.0.0.0", port=8000, app=app)


