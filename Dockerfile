# Start with a Python image.
FROM frolvlad/alpine-python3
# Some stuff that everyone has been copy-pasting
# since the dawn of time.

ENV PYTHONUNBUFFERED 1

# RUN mkdir /code
WORKDIR /code
COPY "./requirements.txt" "./"
COPY "./package.json" "./"

RUN apk add --no-cache --update bash postgresql-dev python3-dev musl-dev netcat-openbsd zlib-dev jpeg-dev yarn

RUN apk add --no-cache --virtual build-dependencies linux-headers gcc \
   && pip3 install -U pip && pip3 install -Ur requirements.txt \
   && yarn install && yarn \
   && apk del build-dependencies

COPY "./" "./"
# COPY "./entrypoint.sh" "./entrypoint.sh"

RUN chown -hR nobody:nobody /code/ && chmod -R 775 /code/ && chmod +x /code/entrypoint.sh

USER nobody
ENTRYPOINT ["/code/entrypoint.sh"]
#&& python3 manage.py collectstatic && rm -rf node_modules \
EXPOSE 80