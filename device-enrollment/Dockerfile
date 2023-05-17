FROM python:3.8.4-slim

# setup environment variable
ENV DockerHOME=/code

# set work directory
RUN mkdir -p $DockerHOME

# set work directory
WORKDIR $DockerHOME

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy code
COPY ./common $DockerHOME/common
COPY ./device-enrollment/main.py $DockerHOME/main.py
COPY ./device-enrollment/requirements.txt $DockerHOME/requirements.txt

EXPOSE 2770
# install dependencies
RUN pip install -r requirements.txt