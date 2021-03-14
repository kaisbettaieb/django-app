FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/ayomi
WORKDIR /usr/src/ayomi
USER root

COPY requirements.txt /usr/src/ayomi
RUN pip install -r requirements.txt

COPY app/ /usr/src/ayomi/app
COPY templates/ /usr/src/ayomi/templates