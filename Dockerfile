
FROM ubuntu:18.04

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip3 install -r requirements.txt
EXPOSE 8000
