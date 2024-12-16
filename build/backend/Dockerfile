FROM python:3.11-slim-buster

COPY build/backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY /app /app

EXPOSE 8000

CMD ["python", "app/app.py"]