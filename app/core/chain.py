from dotenv import load_dotenv

load_dotenv(".env")

from langchain_groq.chat_models import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from httpx import Client

from core.qdrant import qvs
from core.format import format_docs
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

llm = ChatGroq(
    model="gemma2-9b-it",
    max_tokens=2048,
    http_client=Client(proxy=settings.proxy),
)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | template
    | llm
    | StrOutputParser()
)
