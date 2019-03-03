![tf_aws_docker](https://s3-ap-southeast-2.amazonaws.com/innablr/tf_aws_docker.png)

## Docker Image.

### Overview
I am using Docker with Ubuntu Server 18.04 running on AWS EC2 to create this image.

### Setup

Using the following Dockerfile configuration:

```
FROM ubuntu:18.04

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip3 install -r requirements.txt
EXPOSE 8000

```

This completes setup of a containerised Ubuntu image running python3 with Django==2.0 and djangorestframework==3.9.1.
To create an image from the Dockerfile, assuming docker is already installed on your machine, run this command from the same directory:

```
docker build .
```

The image can then be pushed to your repo using:

```
docker tag 3a59493e9d98 jackalack117/innablr_image
docker push jackalack117/innablr_image  
```

The docker image for this project is available at:

[](https://cloud.docker.com/repository/docker/jackalack117/innablr_image)
