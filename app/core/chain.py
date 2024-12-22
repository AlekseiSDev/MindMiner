from dotenv import load_dotenv

load_dotenv(".env")

from httpx import Client
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_gigachat import GigaChat
from langchain_groq.chat_models import ChatGroq

from core.format import format_docs
from core.qdrant import qvs
from core.settings import settings

retriever = qvs.as_retriever(search_type="similarity", search_kwargs={"k": 5})

template = ChatPromptTemplate(
    [
        (
            "human",
            "Ты - помощник для ответа на вопросы по базе знаний пользователя. Используй контекст ниже для ответа на вопросы пользователя. Если ты не знаешь ответ на вопрос, так и скажи. В конце ответа указывай список источников (со ссылками), из которых была использована информация. Важно: ответ должен быть на русском языке вне зависимости от языка документа.\n Вопрос пользователя: {question} \n Контекст из базы знаний: {context} \nAnswer:",
        )
    ]
)

def get_llm(model_name: str = "ChatGroq"):
    if model_name == "ChatGroq":
        return ChatGroq(
            model="gemma2-9b-it",
            max_tokens=2048,
            http_client=Client(proxy=str(settings.proxy)),
        )
    elif model_name == "GigaChat":
        return GigaChat(
            model="GigaChat-Pro",
            credentials=str(settings.giga_api_key),
            timeout=30,
            verify_ssl_certs=False
        )
    else:
        raise ValueError(f"Model {model_name} is not supported.")

def get_rag_chain(llm: str = "ChatGroq", top_k: int = 5):
    retriever.search_kwargs = {"k": top_k}

    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | template
        | get_llm(llm)
        | StrOutputParser()
    )
