import pandas as pd
import glob
from dotenv import dotenv_values
import os
import openai
import time
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import pandas as pd
import glob
from dotenv import dotenv_values
import os
import openai
import time
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import hashlib
from datetime import datetime

from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA #-> for retrieval QA
from langchain.chains.question_answering import load_qa_chain #-> for load QA 
from langchain.document_loaders import TextLoader, PyPDFLoader, DataFrameLoader #-> types of data loader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter #-> to splits data to chunks
from langchain.vectorstores import Chroma, FAISS #to create a db of chunks
from langchain.embeddings import OpenAIEmbeddings #embeddings
from langchain.embeddings import OpenAIEmbeddings #embeddings
from langchain.vectorstores import Chroma #to create a db of chunks

from langchain.llms import OpenAI #-> for Large Language Model
from langchain.chains.question_answering import load_qa_chain

from langchain.vectorstores import Chroma, FAISS #to create a db of chunks
from langchain.embeddings import OpenAIEmbeddings #embeddings

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 15000,
    chunk_overlap  = 200,
    length_function = len,
)



config = dotenv_values(".env")
# config["OAI"]
openai.api_key = config["OAI"]
os.environ["OPENAI_API_KEY"] = config["OAI"]

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

tokenizer = tiktoken.get_encoding('cl100k_base') 

# create the length function
def tiktoken_len(text):
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)


model_name = 'text-embedding-ada-002'

embed = OpenAIEmbeddings(openai_api_key=config["OAI"]
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=10,
    length_function=tiktoken_len,
    separators=["\n\n", "\n", " ", ""]
)

def svt(N,c):
    with open(N, 'w', encoding='utf-8') as f:
        f.write(c)
    
def ldt(N):
    with open(N, "r", encoding='utf8') as f:
        c = f.read()
    return c
    
def hashme(STR):
    STR = str(STR)
    return str(hashlib.md5(STR.encode('utf-8')).hexdigest())

COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"

COMPLETIONS_API_PARAMS = {
    # We use temperature of 0.0 because it gives the most predictable, factual answer.
    "temperature": 0.1,
    "max_tokens": 6000,
    "model": COMPLETIONS_MODEL,
}   

def getAnswer(prompt):


    response = openai.Completion.create(
                prompt=prompt,
                **COMPLETIONS_API_PARAMS
            )

    answer = response["choices"][0]["text"].strip(" \n")

    if not os.path.isdir('.cache'):
        os.mkdir(".cache")

    cached = str(int(time.time()))

    with open(".cache/"+cached+'.txt', 'w') as f:
        f.write(prompt + "\n\n\n\n" + answer)

    return answer

def ask_GPT4(system_intel, prompt): 
    now = datetime.now() # current date and time2
    result = openai.ChatCompletion.create(model="gpt-4",
                                 messages=[{"role": "system", "content": system_intel},
                                           {"role": "user", "content": prompt}])
    if not os.path.isdir('.cache'):
        os.mkdir(".cache")
    now2 = datetime.now() # current date and time


    date_time = now.strftime("%m/%d/%Y, %H:%M:%S") + " --> " + now2.strftime("%m/%d/%Y, %H:%M:%S")
    print("NOW:",date_time)	

    cached = str(int(time.time()))
    answer =result['choices'][0]['message']['content']

    with open(".cache/"+cached+'.txt', 'w') as f:
        f.write(system_intel + "\n\n\n\n" + prompt + "\n\n\n\n" + answer)
    return answer

def ask_GPT3(system_intel, prompt): 
    now = datetime.now() # current date and time2
    result = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k-0613",
                                 messages=[{"role": "system", "content": system_intel},
                                           {"role": "user", "content": prompt}])
    if not os.path.isdir('.cache'):
        os.mkdir(".cache")
    now2 = datetime.now() # current date and time


    date_time = now.strftime("%m/%d/%Y, %H:%M:%S") + " --> " + now2.strftime("%m/%d/%Y, %H:%M:%S")
    print("NOW:",date_time)	

    cached = str(int(time.time()))
    answer =result['choices'][0]['message']['content']

    with open(".cache/"+cached+'.txt', 'w') as f:
        f.write(system_intel + "\n\n\n\n" + prompt + "\n\n\n\n" + answer)
    return answer

