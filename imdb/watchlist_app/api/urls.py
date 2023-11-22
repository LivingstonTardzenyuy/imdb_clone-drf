from django.urls import path 
from watchlist_app.api.views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('movie/<int:pk>/', movie_details, name = 'movie-details'),
]
