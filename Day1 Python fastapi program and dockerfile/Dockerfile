FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install fastapi[all] uvicorn

EXPOSE 8000

ENV FASTAPI_APP=main:app

CMD [ "uvicorn","main:app", "--host", "0.0.0.0", "--port", "8000"]