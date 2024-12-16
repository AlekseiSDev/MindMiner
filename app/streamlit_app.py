import streamlit as st
import requests
from core.settings import settings

q = st.text_input("Ваш вопрос")

if st.button("Найти"):
    ans = requests.get(
        settings.fastapi_host + "http://localhost:8000/ask", params={"user_question": q}
    ).json()["answer"]
    st.markdown(ans)

path = st.text_input("Путь к документу")
text = st.text_area("Содержимое документа")

if st.button("Загрузить"):
    requests.post(settings.fastapi_host + "update", json=[{"path": path, "text": text}])
