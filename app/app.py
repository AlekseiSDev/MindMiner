import uvicorn

from fastapi import FastAPI, HTTPException, Query
from typing import Annotated, List

from core.chain import rag_chain
from core.update import update_collection
from core.settings import settings
from api.schemas import LLMAnswer, Document

app = FastAPI()


@app.get("/ask", response_model=LLMAnswer)
async def generate_answer(
    user_question: Annotated[str, Query(description="Вопрос пользователя")],
):
    try:
        answer_text = rag_chain.invoke(user_question, verbose=True)
        return LLMAnswer(answer=answer_text)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error generating answer: {str(e)}"
        )


@app.post("/update")
def update_database(docs: List[Document]):
    for doc in docs:
        update_collection(doc.path, doc.text)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.fastapi_host.host, port=settings.fastapi_host.port)
