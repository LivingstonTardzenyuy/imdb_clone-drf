from django.urls import path 
from watchlist_app.api.views import *

urlpatterns = [
    path('', WatchListList.as_view(), name = 'home'),
    path('watchlist/<int:pk>/', WatchListDetails.as_view(), name = 'watchlist-details'),


    path('streamplatform/', StreamPlatFormList.as_view(), name = 'streamplatform'),
    path('streamplatform/<int:pk>/', StreamPlatFormDetails.as_view(), name = 'streamplatform-detail'),


    path('reviews/', ReviewsList.as_view(), name = "reviews"),
]

