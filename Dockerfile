FROM python:3.12

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 8000


RUN pip install --no-cache-dir -r /tmp/requirements.txt