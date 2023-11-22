from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializers
from django.shortcuts import redirect
from rest_framework import status


@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializers = MovieSerializers(movie, many = True)
        return Response(serializers.data, status = status.HTTP_200_OK)

    if request.method == 'POST':
        serializers = MovieSerializers(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except MovieDoesNotExists():
            return Response({"error: Movie not found"}, status = status.HTTP_404_NOT_FOUND)
        
        serializers = MovieSerializers(movie)
        return Response(serializers.data, status = status.HTTP_200_OK)

    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializers = MovieSerializers(movie, data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status = status.HTTP_404_NOT_FOUND)


    if request.method == 'DELETE':
        movie = Movie.objects.get(pk = pk)
        movie.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



