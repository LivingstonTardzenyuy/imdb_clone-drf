from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie

@api_view(['GET'])
def home(request):
    movie = Movie.objects.all()
    return JsonResponse(movie.data)