FROM python:3.7.4-slim

# set work directory
WORKDIR /usr/src/langsitebuilder

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/langsitebuilder/Pipfile
RUN pipenv install --skip-lock --system --dev

# copy project
COPY . /usr/src/langsitebuilder/