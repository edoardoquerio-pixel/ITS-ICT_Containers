FROM ubuntu:latest

LABEL MANTAINER="Edoardo Querio Gianetto"

USER root

RUN apt update && \ 
    apt install -y redis-server

EXPOSE 6380/tcp

USER redis

COPY ./redis.conf /etc/redis/redis.conf 

ENTRYPOINT ["redis-server", "/etc/redis/redis.conf"] 

