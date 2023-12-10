from rest_framework.decorators import api_view 
from rest_framework.response import Response
from user_app.api.serializers import RegistrationSerializer

@api_view(["POST",])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # HTTP 201 Created for successful registration
        else:
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request for invalid data
