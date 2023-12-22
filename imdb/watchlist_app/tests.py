from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
 

from watchlist_app.api import serializers 
from watchlist_app import models

class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(username = "example", password = "Password@123")
        #Login in a user. 
        self.token = Token.objects.get(user__username = self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
    def test_streamPlatFormCreate(self):
        data = {
            "name": "kongyuylivingston",
            "about": "best movie on earth",
            "website": "www.kongnyuy.com",
        }
        
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)