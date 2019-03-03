![tf_aws_docker](https://s3-ap-southeast-2.amazonaws.com/innablr/tf_aws_docker.png)

## Packing the Django REST API app.

### Overview
I am using Docker with Docker compose on the AWS AMI of Ubuntu Server 18.04.1 LTS. To get started with Docker on Ubuntu:

```
sudo apt-get install -y docker.io
```

When the install is complet, check the version. I am using 18.06.1-ce:

```
docker version
```

Once you have verified a successful install, you will need to also install docker compose. Compose allows us to configure the application via yaml. Download the latest version of compose, I am using 1.23.2 but the versions can change so be sure to edit the below link accordingly:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Update the security persmissions:

```
sudo chmod +x /usr/local/bin/docker-compose
```

Once completed, we can now create a docker file which is a list of instructions that docker should follow when creating our image. Docker has two stages, build and run. The build stage will create the container image that we can run our application with. Create a new un-associated Dockerfile in your code directory 'touch Dockerfile':

```
FROM python:3 # Bases the image from a python configuration.

ENV PYTHONUNBUFFERED 1    # Creates our environment variable 'PYTHONUNBUFFERED', sets the output to non buffered in the std in/out.
RUN mkdir /    # Creates the container directory for our source code.  
WORKDIR /code    # This is the working directory used to interact with the container.
COPY . /code/    # Copies all the project files to the container.
RUN pip install -r requirements.txt    # The list of requirements for the application.
```

Now we can configure the docker compose file. Create the file in the directory using the same command as above 'touch docker-compose.yml':

```
version: '3'    # Specifies the syntax version used.

services:
  web:
    build: .
    command: bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    container_name: innablr_container
    volumes:
      - .:/code
    ports:
      - "8000:8000

```

Now we can run our migration command to migrate the applications database. We use the following docker compose run command to do this:

```
sudo docker-compose run web python manage.py migrate
```

Once this command has completed execution we can start the container:

```
sudo docker-compose up
```
