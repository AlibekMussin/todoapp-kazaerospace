FROM python:3.8.3-slim-buster

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .
# create logs directory
RUN mkdir -p logs

CMD gunicorn -b 0.0.0.0:8000 todoapp.wsgi