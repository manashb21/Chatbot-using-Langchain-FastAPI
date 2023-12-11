from langchain.llms import CTransformers
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

#initializing the model
llm = CTransformers(model = "model", 
                    model_file = "llama-2-7b-chat.Q4_K_M.gguf",
                    config = {'max_new_tokens' : 1024,
                              'repetition_penalty': 1.1,
                              'temperature': 0.8,
                            'context_length' : 8192},
                    callbacks = [StreamingStdOutCallbackHandler()])

template = """
[INST] <<SYS>>
You are a helpful, respectful and honest assistant who answers questions about technology, coding, and IT. 
Your answers are to the point and always brief. 
You donot provide information or answer about socio-cultural, racial, political and any sensitive topic and incase 
those topics are asked, just say you don't know and stop explaining. 

If you don't know answer about something, say you don't know. Donot create your own answer.
<</SYS>>
{text}[/INST]
"""

prompt = PromptTemplate(template=template, input_variables=["text"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

def generate_response(query):
    return(llm_chain.run(query))
