# Continuous integration, testing and deployment. 

[![Build Status](https://travis-ci.org/bransfieldjack/Innablr-Technical-Challenge.svg?branch=master)](https://travis-ci.org/bransfieldjack/Innablr-Technical-Challenge)

![travoku](https://s3-ap-southeast-2.amazonaws.com/innablr/travoku.png)

My pipeline for this app is defined as follows:

Dev (AWS) > Travis Testing Server > Heroku Staging Environment > Heroku Production Environment

***

[Travis Server](https://travis-ci.org/bransfieldjack/Innablr-Technical-Challenge)

Staging: [Heroku Staging](https://innablr-staging.herokuapp.com/)

Production: [Heroku Production](https://innablr-production.herokuapp.com/)

## Mechanism

Any newly deployed code pushed to the Master branch of my repo will automatically trigger a build with Travis. Travis will run the following configuration file:

```
language: python
python:
    - "3.4"
before_install:
  - chmod a+x manage.py
install: "pip install -r requirements.txt"
env:
  - DJANGO=2.0
services:
  - postgresql
script:
  - python3 manage.py test
  - sudo apt-get update
  - git rev-parse --verify HEAD

```

I'm having an issue at the moment where the version of python that I am using is causing issues with my Django test cases. I believe it to be an issue with encoding, see [TypeError: 'str' does not support the buffer interface](https://stackoverflow.com/questions/5471158/typeerror-str-does-not-support-the-buffer-interface)

If the testing completes with success on the Travis server, a heroku staging environment will automatically run a build job via the procfile and requirements.txt contained in the repo. If the build completes with success we have the option to manually promote to production. (Heroku will only successfully automate a build from your Master branch)

![heroku pipeline](https://s3-ap-southeast-2.amazonaws.com/innablr/heroku+pipeline.PNG)
