import os
from dotenv import load_dotenv
load_dotenv()
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain import hub
from langchain.document_loaders import DirectoryLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

app = FastAPI()

class Query(BaseModel):
    question: str

class RAGService:
    def __init__(self, directory_path: str):
        loader = DirectoryLoader(
            directory_path,
            glob="**/*.md",
            loader_cls=UnstructuredMarkdownLoader,
            loader_kwargs={"encoding": "utf-8"}
        )
        docs = loader.load()
        
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = splitter.split_documents(docs)
        
        embeddings = OpenAIEmbeddings()
        self.vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
        self.retriever = self.vectorstore.as_retriever()
        
        prompt = hub.pull("rlm/rag-prompt")
        
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        
        self.rag_chain = (
            {"context": self.retriever | self.format_docs, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
    
    @staticmethod
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    def answer_question(self, question: str) -> str:
        try:
            return self.rag_chain.invoke(question)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# Initialize the RAG service on startup
@app.on_event("startup")
def startup_event():
    global rag_service
    directory_path = "data/lesha_obsi_sample"
    rag_service = RAGService(directory_path)

@app.post("/ask")
def ask_question(query: Query):
    answer = rag_service.answer_question(query.question)
    return {"answer": answer}
