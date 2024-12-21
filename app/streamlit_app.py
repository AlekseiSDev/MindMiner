import streamlit as st
import requests
from core.settings import settings

q = st.text_input("Ваш вопрос")

model_choice = st.selectbox("Выберите модель:", ["ChatGroq", "GigaChat"])

if st.button("Найти"):
    try:
        ans = requests.get(
            str(settings.fastapi_host) + "ask", 
            params={"user_question": q, "model": model_choice}
        ).json()["answer"]
        st.markdown(ans)
    except Exception as e:
        st.warning(f'Бэк еще не проснулся или с ним что-то не так!\n{e}', icon="⚠️")

path = st.text_input("Путь к документу")
text = st.text_area("Содержимое документа")

if st.button("Загрузить"):
    requests.post(
        str(settings.fastapi_host) + "update", json=[{"path": path, "text": text}]
    )
