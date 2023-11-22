from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import * 

@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome to the home view!"})