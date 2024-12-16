import streamlit as st
import requests
from core.settings import settings

q = st.text_input("Ваш вопрос")

if st.button("Найти"):
    st.text(str(settings.fastapi_host) + "/ask")
    try:
        ans = requests.get(
            str(settings.fastapi_host) + "ask", params={"user_question": q}
        ).json()["answer"]
        st.markdown(ans)
    except Exception as e:
        print(e)

path = st.text_input("Путь к документу")
text = st.text_area("Содержимое документа")

if st.button("Загрузить"):
    requests.post(
        str(settings.fastapi_host) + "update", json=[{"path": path, "text": text}]
    )
