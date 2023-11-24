from rest_framework import serializers 
from watchlist_app.models import Movie

class MovieSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movie 
        fields = "__all__"


    
    def validate(self, data):
        if data['name'] == data['description']:
            return serializers.ValidationError("the names and description should be different")
        else:
            return data 
