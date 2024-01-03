# ChatBot_Langchain

**Chatbot** using Open Source Large Language Model and LangChain with API endpoints.

Open source LLM used : Llama 2 7B model (quantized gguf model downloaded from HuggingFace, implemented by The Bloke)
Create API endpoint using: FastAPI

**Starting the api**: uvicorn testing:app --reload

**Making the request**: http POST http://127.0.0.1:8000/stream message="Hello?" "access_token:llamaxllama7b"

*OR*,

**DO**: python send_request.py
