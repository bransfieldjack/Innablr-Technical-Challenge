![innablr](https://s3-ap-southeast-2.amazonaws.com/innablr/innablr.PNG)

# Innablr-Technical-Challenge

Scenario:

A large micro services project has set course to develop a considerable number of REST API's in the next 12 months. They are aiming to use a standard set of technologies and patterns to bring consistency to their delivery.

As part of this, you are required to build a boilerplate git repository that includes the basic scaffolding required for each team to kickoff their projects.

Your repository should define a comprehensive pipeline that has at least the following stages: test, build, publish.

As part of this, a simple REST API should also be present in the repository that has a root / endpoint that returns a basic "Hello World" message, and a /status endpoint that returns the following response:

```
{
  "myapplication": [
    {
      "version": "1.0",
      "description": "pre-interview technical test",
      "lastcommitsha": "abc57858585"
    }
  ]
}
```

## Toolchain:

Code repository: GitHub
Pipelines: TravisCI
API's programming language: NodeJS or Golang ideally, but feel free to use something you are more accustomed to.
Image repository: Docker Hub

Additional:

Terraform v0.11.11

## Testing

## Deployment
Django Rest Micro Service
Create a new instance in EC2 to setup the boiler plate code that we will package for use with our containers/instances.
Automated deployment can be achieved with the following terraform provider and resource, but for initial configuration I opted to manually create the environment in AWS.
Terraform command:
```
provider "aws" {
	access_key = "${var.access_key}"
	secret_key = "${var.secret_key}"
	region = "${var.region}"
}

resource "aws_instance" "dev" {
	ami = "ami-07a3bd4944eb120a0"
	instance_type = "t2.micro"

	provisioner "remote-exec" {
		inline = [
			"sudo apt-get update",
      "sudo apt-get install python3-pip",
      "pip3 install virtualenv",
      "virtualenv env",
      "virtualenv env source env/bin/activate",
      ""
		]
	}

}
```
Connect to your instance using the security keys of your choice. In this instance I chose to use the Ubuntu Server 18.04 LTS AMI for familiarity reasons.
Login to the instance using "ubuntu@ec2-x-xxx-xx-xxx.ap-southeast-2.compute.amazonaws.com".
Install any updates on the machine with:
```
sudo apt-get update
```
Use the following commands to install pip (required to install a virtual environment, used for isolation of python applications and dependencies on the machine):
```
sudo apt-get install python3-pip
```
Now we can install and activate our virtual environment:
```
pip3 install virtualenv
```
```
virtualenv env
```
```
source env/bin/activate
```
Once the virtual env has been successfully configured, you will see the following (env) indicator preceding your command prompt:

![virtual_env_running.PNG](https://s3-ap-southeast-2.amazonaws.com/innablr/virtual_env_running.PNG)

The next order of business will be to create the 'requirements.txt' file, which will contain a list of dependencies on which the application depends.
```
django==1.7
gunicorn
requests
djangorestframework==3
django-rest-swagger
django-filter

## dev requirements
sphinx
sphinx_rtd_theme
mock
responses
ipdb
ipython

## Test and quality analysis

pylint
coverage
django-jenkins
django-extensions
django-cors-headers

## custom libs:
-e git://github.com/TangentMicroServices/PythonAuthenticationLib.git#egg=tokenauth
```
Build these requirements using the following pip command:
```
pip install -r requirements.txt
```
Now we are ready to create the Django REST framework project.
I opted to use Django REST framework version 3.0, as it is commonly used and support is easily researched.
Django and Django REST framework are similar, it is possible to replicate the same functionality in Django without installing Django REST framework, however this would require the creation of a large amount of custom written code. Django REST framework provides API functionality out of the box (serializers etc.) and so it was the most efficient choice.
Run the following command to start a new project:
```
django-admin startproject innablr_technical_challenge .
```
Note the full stop at the end of the command, this unpacks the project in the current directory.
Next we will need to migrate the existing models, user auth etc. that exist in our project:
```
python manage.py migrate
```
We will also need to create an superuser account to administer the databases. (Django uses an SQLite database which can be run inside of a packaged application container. )
```
python manage.py createsuperuser
```
Follow the prompts to create a username and password of your choice. (Django 1.11 will not allow you to use a common password - no 'password1' etc.)
Now we are ready to create a Django app (or applet) within the Django REST framework project. I have chosen the name of 'API' for the first app:
```
python manage.py startapp api
```
