from rest_framework import serializers 
from .models import Api 

class ApiSerializer(serializers.ModelSerializer): # Shows all the info relevant to my model.
    class Meta:
        model = Api
        fields = ('id', 'version', 'description', 'lastcommitsha')
    
