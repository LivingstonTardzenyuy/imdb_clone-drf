from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
 

from watchlist_app.api import serializers 
from watchlist_app import models

class StreamPlatformTestCase(APITestCase):
    def test_streamPlatFormCreate(self):
        data = {
            "name": "kongyuylivingston",
            "about": "best movie on earth",
            "website": "www.kongnyuy.com",
        }
        
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
