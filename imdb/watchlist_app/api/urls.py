from django.urls import path 
from watchlist_app.api.views import *

urlpatterns = [
    path('', MovieList.as_view(), name = 'home'),
    path('movie/<int:pk>/', MovieDetails.as_view(), name = 'movie-details'),
]
