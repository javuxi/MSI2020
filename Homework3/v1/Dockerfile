FROM python:3.8-alpine as base
RUN apk update && apk add build-base

COPY . /code/
WORKDIR /code
RUN pip install -r requirements.txt

FROM python:3.8-alpine

COPY --from=base /code/ /code
COPY --from=base /usr/local/lib/python3.8 /usr/local/lib/python3.8
COPY --from=base /usr/local/bin/gunicorn /usr/local/bin/gunicorn
WORKDIR /code

CMD ["python", "app.py"]