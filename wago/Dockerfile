# Start with a Python image.
FROM frolvlad/alpine-python3
# Some stuff that everyone has been copy-pasting
# since the dawn of time.
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN apk add --no-cache --update bash postgresql-dev python3-dev musl-dev uwsgi netcat-openbsd zlib-dev jpeg-dev

RUN apk add --no-cache --virtual build-dependencies  linux-headers   gcc   \
   &&  pip3 install -U pip && pip3 install -Ur requirements.txt \ 
   &&  apk del build-dependencies 

