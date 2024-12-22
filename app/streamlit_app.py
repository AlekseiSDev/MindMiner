import re
import requests
import streamlit as st
from core.instruction import default_instruction, custom_instructions
from core.settings import settings

q = st.text_input("Ваш вопрос")

model_choice = st.selectbox("Выберите модель:", ["ChatGroq", "GigaChat"])

top_k = st.slider("Количество результатов (top_k):", min_value=1, max_value=10, value=5)

use_default_instruction = st.checkbox("Использовать системную инструкцию по умолчанию", value=True)

templates = [{"name": name, "instruction": instruction} for name, instruction in custom_instructions.items()]

# Перемещаем выбор шаблонов в сайдбар
selected_template_idx = st.sidebar.radio("Выберите шаблон инструкции", options=[template["name"] for template in templates])

# Проверяем, если в session_state еще нет значения, то создаем
if "custom_instruction" not in st.session_state:
    st.session_state.custom_instruction = ""

# Сначала обновляем значение custom_instruction, если выбрали новый шаблон
if selected_template_idx:
    selected_template = next(template["instruction"] for template in templates if template["name"] == selected_template_idx)
    if not use_default_instruction:  # Если пользователь не выбрал системную инструкцию
        st.session_state.custom_instruction = selected_template
    else:
        st.session_state.custom_instruction = ""

custom_instruction = st.text_area(
    "Кастомная инструкция (будет игнорироваться, если выбрана системная инструкция)",
    value=st.session_state.custom_instruction if not use_default_instruction else "",
    placeholder="Введите свою инструкцию здесь...",
    height=200
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
