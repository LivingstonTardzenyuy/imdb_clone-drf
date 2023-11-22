from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializers

@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializers = MovieSerializers(movie, many = True)
        return Response(serializers.data)

    if request.method == 'POST':
        serializers = MovieSerializers(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)


@api_view(['GET', 'PUT'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except MovieDoesNotExists():
            return Response(serializers.errors)
        
        serializers = MovieSerializers(movie)
        return Response(serializers.data)

    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializers = MovieSerializers(movie, data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)




