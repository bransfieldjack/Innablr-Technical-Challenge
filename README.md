


## Django Rest

Create a new instance in EC2 to setup the boiler plate code that we will package for use with our containers/instances. Automated deployment can be achieved with the following terraform provider and resource, but for initial configuration I opted to manually create the environment in AWS.

### Terraform:

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

Connect to your instance using the security keys of your choice. In my case I chose to use the Ubuntu Server 18.04 LTS AMI for familiarity reasons. Login to the instance using "ubuntu@ec2-x-xxx-xx-xxx.ap-southeast-2.compute.amazonaws.com".

A run through of the initial configuration commands to prep the environment for Django/Django REST:

```
sudo apt-get update
```
Its import to make sure you are using python3, Django version 2.0 and Django 3.9.1 depend on it. You will also require it before you can begin using pip3. Use the following commands to install pip (required to install a virtual environment, used for isolation of python applications and dependencies on the machine):
```
sudo apt-get -y install python3-pip
```
Now we can install and activate our virtual environment:
```
sudo pip3 install virtualenv
```
```
virtualenv env
```
```
source env/bin/activate
```

Once the virtual env has been successfully configured, you will see the following (env) indicator preceding your command prompt:

![virtual_env_running.PNG](https://s3-ap-southeast-2.amazonaws.com/innablr/virtual_env_running.PNG)

The next order of business will be to create the 'requirements.txt' file, which will contain a list of dependencies on which the application depends. Initially we wont require much, but these will be added to when we are using docker etc.
```
Django==2.0
djangorestframework==3.9.1
```
Build these requirements using the following pip command:
```
pip install -r requirements.txt
```
Now we are ready to create the Django REST framework project.
Django and Django REST framework are similar, it is possible to replicate the same functionality in Django without installing Django REST framework, however this would require the creation of a large amount of custom written code. Django REST framework provides API functionality out of the box (serializers etc.) and so it was the most efficient choice.
Run the following command to start a new project:

```
django-admin startproject innablr_technical_challenge .
```

Note the full stop at the end of the command, this unpacks the project in the current directory. Next we will need to migrate the existing models, user auth etc. that exist in our project:

```
python manage.py migrate
```

We will also need to create a superuser account to administer the databases. (Django uses an SQLite database which can be run inside of a packaged application container. )

```
python manage.py createsuperuser
```

Follow the prompts to create a username and password of your choice. (Django 1.11 will not allow you to use a common password - no 'password1' etc.) Now we are ready to create a Django app (or applet) within the Django REST framework project. I have chosen the name of 'API':

```
python manage.py startapp api
```

Next we will navigate to the settings.py file. Under installed apps, add the 'rest_framework' app and 'api' app names.

![installed_apps](https://s3-ap-southeast-2.amazonaws.com/innablr/installed_apps.PNG)

Now we can update the url endpoint paths (api/urls.py):

```
from django.contrib import admin
from django.urls import path, include
from api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls'))
]

```

Next, setup the models we will use with api/models.py:

```
from django.db import models


class Api(models.Model):
    version = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    lastcommitsha = models.CharField(max_length=50)
```

This creates basic CharField items as per the challenge specifications. The next task is to setup our serializer. The serializer allows for complex querysets to be converted into widely usable JSON format. This is the reason for choosing Django REST framework, as the functionality comes included out of the box. Whilst you can explicitly define your own serializer, standard use cases are catered for with the included functionality. Create a serializers.py file in the api app folder:

```
from rest_framework import serializers
from .models import Api

class ApiSerializer(serializers.ModelSerializer): # Shows all the info relevant to my model.
    class Meta:
        model = Api
        fields = ('id', 'version', 'description', 'lastcommitsha')
```

The api view functionality has been setup with the Djago REST frameworks model viewset classes:

```
from django.shortcuts import render
from rest_framework import viewsets
from .models import Api
from .serializers import ApiSerializer


class ApiView(viewsets.ModelViewSet):
    queryset = Api.objects.all() # Query the DB to return all objects - simple.
    serializer_class = ApiSerializer

```

With the views in place, we can update the urls in the api app. For this we are using the standardrouter() functionality provided. See below:

```

from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers # Generates the URLS for my model.

router = routers.DefaultRouter() # Instantiate the default router.
router.register('api', views.ApiView) # Register the views that I have.

urlpatterns = [
    path('', include(router.urls)) # Creates the nice API html view that we see, no need for additional ex swagger/postman.
]

```

You should now be in a position to test access to the API root.

![api_root](https://s3-ap-southeast-2.amazonaws.com/innablr/api_root.PNG)

## Testing

Some basic unit tests have been added to the api/test.py applet in the application. These test basic get put and post requests.
Test code:
```
from django.test import TestCase
from rest_framework.test import APIRequestFactory


# As per the standard documentation: https://www.django-rest-framework.org/api-guide/testing/


class TestDjango(TestCase):


    def test_requests(self):

        factory = APIRequestFactory()

        self.post_request = factory.post('/api/', {'version': 'test'})
        self.get_request = factory.get('/api/', {'id': '1'})
        self.put_request = factory.put('/api/', {
            'id': '3',
            'version': 'test2',
            'decsription': 'put_request test',
        })
```
