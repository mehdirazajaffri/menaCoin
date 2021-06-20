FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /src
RUN mkdir /static

WORKDIR /src

ADD requirements.txt /src/
RUN pip install -r requirements.txt

ADD . /src