from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializers
from django.shortcuts import redirect
from rest_framework import status

from rest_framework.views import APIView

class MovieList(APIView):
    def get(self, request, format = None):
        movie = Movie.objects.all()
        serializers = MovieSerializers(movie, many = True)
        return Response(serializers.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializers = MovieSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetails(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk = pk)
        except Movie.DoesNotExist:
            return Response({"error": "Movie does not exist"}, status = status.HTTP_404_NOT_FOUND)
        serializers = MovieSerializers(movie)
        return Response(serializers.data, status = status.HTTP_200_OK)


    def post(self, request, pk):
        movie = Movie.objects.get(pk = pk)
        serializers = MovieSerializers(movie, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Movie.objects.get(pk = pk)
        movie.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
