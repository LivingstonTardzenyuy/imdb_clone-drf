from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from watchlist_app.models import *

from watchlist_app.api import serializers 
from watchlist_app import models

class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(username = "example", password = "Password@123")
        #Login in a user. 
        self.token = Token.objects.get(user__username = self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        
        self.stream = StreamPlatForm.objects.create(
            name = "netflix",
            about = ""
        )
        
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
        
        
    def test_streamplatform_id(self):
        response = self.client.get(reverse('streamplatform-detail', args = (self.stream.id,)))      #args allow me to access the individual elements. 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    # def test_stramplatform
class WatchlistTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="kongnyuy", password="Password@123")
        self.token = Token.objects.get(user__username = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = 'Token' + self.token.key)
        
        self.stream = StreamPlatForm.objects.create(
            name="Netflix",
            about="The movie of the gold",
            website="www.abakwa.com"
        
        )
        
        self.watchlist = models.WatchList.objects.create(platform = self.stream, title="example movies", description="Example movie", active=True)
    
    def test_watchlist_create(self):
        data = {
            "title": "Abakwa",
            "description": "the movie that will be great for all",
            "platform": self.stream,
            "active": True 
        }
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_watchlist_ind(self):
        response = self.client.get(reverse('movie-detail', args = (self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.get().title, "example movies")
        self.assertEqual(models.WatchList.objects.count(), 1)
        
    # def test_watchlist_delete(self):
    #     response = self.client.delete(reverse('movie-detail', args=(self.watchlist.id,)))
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username = self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)
        
        self.stream = models.StreamPlatForm.objects.create(
            name="Netflix",
            about="#1 platform",
            website="www.abakwa.com"
        )
        
        self.watchlist = models.WatchList.objects.create(
            platform = self.stream,
            title = 'the pride of abakwa',
            description = 'best movie in the city',
            active = 'True'
        )
        
        
        