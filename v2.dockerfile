FROM ubuntu:xenial

RUN apt-get update && apt-get install -y python

COPY . /kubehacksession
WORKDIR /kubehacksession

ENTRYPOINT ["python", "v2.py"]
