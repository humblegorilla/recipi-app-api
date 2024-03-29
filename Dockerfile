FROM python:3.9-alpine3.13
LABEL maintainer="bga.dev"

ENV PYTHONUNBUFFERED 1

# Create and set working directory
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
# Install dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --no-cache postgresql-client  && \
    apk add --no-cache --virtual .tmp-docker-volumes \
    build-base postgresql-dev musl-dev && \
    if [ "$DEV" = "true" ] ; \ 
    then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-docker-volumes && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user

ENV PATH="/py/bin:$PATH"

USER django-user
