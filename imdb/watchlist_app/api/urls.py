from django.urls import path 
from watchlist_app.api.views import *

urlpatterns = [
    path('', WatchListList.as_view(), name = 'home'),
    path('watchlist/<int:pk>/', WatchListDetails.as_view(), name = 'watchlist-details'),


    path('streamplatform/', StreamPlatFormList.as_view(), name = 'streamplatform'),

    path('streamplatform/<int:pk>/reviews/', StreamPlatFormDetails.as_view(), name = 'streamplatform-detail'),          #allows me to access alll reviews for a particular movie. 
    

    
    path('stream/<int:pk>/reviews/', ReviewsList.as_view(), name = 'review-detials'),            #accessing individual reviews. 
    path('stream/<int:pk>/reviews-create', ReviewsCreate.as_view(), name = 'review-create'),
    path('stream/review/<int:pk>/', ReviewsListDetails.as_view(), name = "reviews"),
]

