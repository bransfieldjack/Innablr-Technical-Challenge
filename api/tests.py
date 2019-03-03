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
        
        
