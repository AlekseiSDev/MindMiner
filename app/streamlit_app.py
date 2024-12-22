import re
import requests
import streamlit as st
from core.instruction import default_instruction
from core.settings import settings

q = st.text_input("Ваш вопрос")

model_choice = st.selectbox("Выберите модель:", ["ChatGroq", "GigaChat"])

top_k = st.slider("Количество результатов (top_k):", min_value=1, max_value=10, value=5)

use_default_instruction = st.checkbox("Использовать системную инструкцию по умолчанию", value=True)
custom_instruction = st.text_area(
    "Кастомная инструкция (будет игнорироваться, если выбрана системная инструкция)", 
    placeholder="Введите свою инструкцию здесь..."
)

def is_valid_instruction(instruction: str) -> bool:
    question_count = len(re.findall(r"\{question\}", instruction))
    context_count = len(re.findall(r"\{context\}", instruction))
    return question_count == 1 and context_count == 1

if st.button("Найти"):
    try:
        if not use_default_instruction and not is_valid_instruction(custom_instruction):
            st.warning("В кастомной инструкции должно быть по одному вхождению {question} и {context}.")
        else:
            instruction = default_instruction if use_default_instruction else custom_instruction
        
            ans = requests.get(
                str(settings.fastapi_host) + "ask", 
                params={
                    "user_question": q, 
                    "model": model_choice, 
                    "top_k": top_k, 
                    "instruction": instruction
                },
                timeout=10
            ).json()["answer"]
            
            st.markdown(ans)
    except Exception as e:
        st.warning(f'Бэк еще не проснулся или с ним что-то не так!\n{e}', icon="⚠️")

path = st.text_input("Путь к документу")
text = st.text_area("Содержимое документа")

if st.button("Загрузить"):
    requests.post(
        str(settings.fastapi_host) + "update", json=[{"path": path, "text": text}],
        timeout=10
    )
