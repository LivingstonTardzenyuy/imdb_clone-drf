from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import WatchList, StreamPlatForm
from watchlist_app.api.serializers import WatchListSerializers, StreamPlatFormSerializers
from django.shortcuts import redirect
from rest_framework import status

from rest_framework.views import APIView


class StreamPlatFormList(APIView):
    def get(self, request, format = None):
        streamplatform = StreamPlatForm.objects.all()
        serializers = StreamPlatFormSerializers(streamplatform, many = True)
        return Response(serializers.data, status = status.HTTP_200_OK)


    def post(self, request):
        serializer = StreamPlatFormSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)




class WatchListList(APIView):
    def get(self, request, format = None):
        watchlist = WatchList.objects.all()
        serializers = WatchListSerializers(watchlist, many = True)
        return Response(serializers.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializers = WatchListSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetails(APIView):
    def get(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk = pk)
        except WatchList.DoesNotExist:
            return Response({"error": "WatchList does not exist"}, status = status.HTTP_404_NOT_FOUND)
        serializers = WatchListSerializers(watchlist)
        return Response(serializers.data, status = status.HTTP_200_OK)


    def post(self, request, pk):
        watchlist = WatchList.objects.get(pk = pk)
        serializers = WatchListSerializers(watchlist, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        watchlist = WatchList.objects.get(pk = pk)
        watchlist.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
