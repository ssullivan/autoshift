FROM python:3.8-alpine

ENV SHIFT_GAMES='bl3 blps bl2 bl' \
    SHIFT_PLATFORMS='epic steam' \
    SHIFT_ARGS='--schedule' \
    TZ='America/Chicago'

COPY . /autoshift/
RUN apk add --no-cache --virtual .build-deps gcc libc-dev libxslt-dev && \
        apk add --no-cache libxslt && \
        pip install --no-cache-dir lxml>=3.5.0 && \
        apk del .build-deps && \
        pip install -r ./autoshift/requirements.txt && \
        mkdir ./autoshift/data
CMD python ./autoshift/auto.py --user ${SHIFT_USER} --P ${SHIFT_PASS} --games ${SHIFT_GAMES} --platforms ${SHIFT_PLATFORMS} ${SHIFT_ARGS}