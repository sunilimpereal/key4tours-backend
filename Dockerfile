FROM python:3.8.3-alpine
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev  
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
COPY . /app/




