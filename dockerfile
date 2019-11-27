FROM python:3.8-alpine

ENV SHIFT_GAMES='bl3 blps bl2 bl' \
    SHIFT_PLATFORMS='epic steam' \
    SHIFT_ARGS='--schedule' \
    TZ='America/Chicago'

COPY . /autoshift/
RUN apk add --no-cache --virtual .build-deps \
        gcc \
        libc-dev \
        libxml2 \
        libxml2-dev \
        libxslt-dev \
        python3-dev \
        libxslt \
        py3-lxml && \
        set -x && \
        pip install -r ./autoshift/requirements.txt  && \
        apk del .build-deps && \
        mkdir ./autoshift/data
CMD python ./autoshift/auto.py --user ${SHIFT_USER} --P ${SHIFT_PASS} --games ${SHIFT_GAMES} --platforms ${SHIFT_PLATFORMS} ${SHIFT_ARGS}