![innablr](https://s3-ap-southeast-2.amazonaws.com/innablr/innablr.PNG)

# Overview

### Index

[Overview](https://github.com/bransfieldjack/Innablr-Technical-Challenge/tree/overview) (Current branch) An outline of the repo structure and information regarding the challenge.
***
[Django REST API](https://github.com/bransfieldjack/Innablr-Technical-Challenge/tree/django_rest_setup) Details regarding the REST API application, written in python with the Django REST framework.
***
[Infrastructure and deployment](https://github.com/bransfieldjack/Innablr-Technical-Challenge/tree/infrastructre_and_deployment) walkthrough of the deployment and information for auto scaling and infrastructure as code deployment.
***
[Code base and config files](https://github.com/bransfieldjack/Innablr-Technical-Challenge/tree/master) All project files, re-useable.
***
[CI/CD](https://github.com/bransfieldjack/Innablr-Technical-Challenge/tree/master) Continuous integration and testing. 

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
