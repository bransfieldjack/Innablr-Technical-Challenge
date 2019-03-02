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

## Technologies Used

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
