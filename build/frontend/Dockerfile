FROM python:3.11-slim-buster

COPY build/frontend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY /app/streamlit_app.py /app/streamlit_app.py
COPY /app/core/settings.py /app/core/settings.py

EXPOSE 8501

CMD ["streamlit", "run", "/app/streamlit_app.py"]