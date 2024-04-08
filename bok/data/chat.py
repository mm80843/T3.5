import os
import openai
import re
import datetime
import hashlib
import warnings
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

warnings.filterwarnings('ignore')

load_dotenv()



print(openai.__version__)



embeddings = OpenAIEmbeddings()
base_path = "./vectorDB/"
vectordb = Chroma(persist_directory=base_path,embedding_function=embeddings)
print()
print("CHECK:",len(vectordb.get()["ids"]),"elements already stored.")


def create_agent_chain(llm):
    chain = load_qa_chain(llm, chain_type="stuff")
    return chain

def get_llm_response(query,vectordb,temperature=0.1,k=10,seed=""):
    F = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    Q = query+","+str(temperature)+","+str(k)+str(seed)
    Q = hashlib.md5(Q.encode()).hexdigest()
    print(Q)
    FILE = "cache/"+Q+".md"
    if os.path.isfile(FILE):
        with open(FILE,"r") as f:
            A =f.read()
            answer = A.split("\n\n---\n\n>A:\n")[-1].strip()
            docs = A.split("\n\n---\n\n>A:\n")[-2].split("\n\n---\n\nD:\n")[-1].strip()
            docs = re.findall("\'article\': \'(.*?)\'}", docs, re.DOTALL)
    else:   
        llm = ChatOpenAI(
            model="gpt-3.5-turbo-1106",
            temperature=temperature,
        )
        chain = create_agent_chain(llm)
        matching_docs = vectordb.similarity_search(query,k)
        answer = chain.run(input_documents=matching_docs, question=query)
        docs = [x.metadata["article"] for x in matching_docs]
        with open(FILE,"w") as f:
            f.write(">Q:\n"+query +"\n\n---\n\nD:\n"+str(matching_docs)+ "\n\n---\n\n>A:\n"+answer)
    return answer, docs