from django.urls import path 
from watchlist_app.api.views import *

urlpatterns = [
    path('', home, name = 'home'),
]
