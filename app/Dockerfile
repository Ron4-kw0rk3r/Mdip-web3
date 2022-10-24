# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

RUN export DOCKER_BUILDKIT=0
RUN export COMPOSE_DOCKER_CLI_BUILD=0


WORKDIR /app


COPY requeriments.txt requeriments.txt


RUN pip3 install -r  requeriments.txt

COPY . .
CMD [ "python3", "-m" , "flask" ,"--app" ,"app/marketv2.py", "run" , "--host=0.0.0.0"]

