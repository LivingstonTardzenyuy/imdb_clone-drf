from rest_framework import serializers 
from watchlist_app.models import WatchList, StreamPlatForm

class WatchListSerializers(serializers.ModelSerializer):

    length_name = serializers.SerializerMethodField()           #allows me to define a field 

    class Meta:
        model = WatchList 
        fields = "__all__"

    def get_length_name(self, object):
        length = len(object.title)
        return length

    
    def validate(self, data):
        if data['title'] == data['description']:
            return serializers.ValidationError("the title and description should be different")
        else:
            return data 


class StreamPlatFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatForm
        fields = "__all__"