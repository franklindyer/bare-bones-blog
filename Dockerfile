FROM docker.io/python:3.7-slim

ARG email="franklindyer@icloud.com"
LABEL "maintainer"=$email

USER root

RUN mkdir /data
RUN mkdir /data/app
ENV AP /data/app
ENV PORT 8080

RUN apt-get -y update
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN python3 -m pip install bottle markdown bottle_sqlite

COPY ./server.py $AP/

WORKDIR $AP

CMD ["sh", "-c", "python3 server.py ${PORT}"]
