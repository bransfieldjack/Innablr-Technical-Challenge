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

[Innablr Docker Image](https://cloud.docker.com/repository/docker/jackalack117/innablr_image)

***

## Platform Deployment

### Overview

The dev environment for this application is hosted on an EC2 instance in AWS. My pipeline consists of Dev > Travis Test Server > Heroku Staging > Heroku Prod (more on this in the CICD branch of this repository).

### Scalable deployment: AWS ECS with Fargate

Fargate provides a launch type within ECS for container deployment. For this deployment, we will want to configure a custom container solution.

![custom_container](https://s3-ap-southeast-2.amazonaws.com/innablr/custom_container.PNG)

Rename your containers appropriately, added all relevant configuration details depending on your preference. For this container, I am accessing the docker image created above from the following url: 'jackalack117/innablr_image'. My django rest app is communicating on port 8000, so I have added it to the port mappings. All other VPC and network configurations I have left as default. Make sure your environment essential check box is ticked. This will make sure your containers are stopped if there are errors. Under task definition, I have upgraded the defaults for Task Memory and CPU. (Task Memory: 2G, 1vCPU). I have also configured an application load balancer to listen on port 8000 as well, in order to communicate with the django app. Next, we will configure the service.

![service_starting](https://s3-ap-southeast-2.amazonaws.com/innablr/service_starting.PNG)

Without the service we cannot administer our containers and you cannot proceed without it.
Once all the resources have been created, we can increase the number of tasks to three for the task definition section of the deployment.

We also have the option to configure service auto scaling. This is dependent on the applications needs and the volume of traffic that it will receive obviously. I have added two scaling policies, one for scaling up resources, the other for scaling down:

![scale_up](https://s3-ap-southeast-2.amazonaws.com/innablr/scale_up.PNG)

To access the cluster, find the DNS details of the the load balancer listed in the details section, it should look something like 'EC2Xx-XXXXx-XXXXXXXXXXXX-XXXXXXXXX.ap-southeast-2.elb.amazonaws.com'.

### Automated deployment: Terraform

We can automate the above deployment with terraform using 'infrastructure as code'. All of the configuration files can be found here: [terraform](https://github.com/bransfieldjack/Innablr-Technical-Challenge/tree/master) All of these files can be run from the same .tf file if you want, but you can run into issues if you are trying to provision a resource before another resource that the one you are trying to stand up depends on. For this reason, I recommend splitting the work across multiple configuration files.
