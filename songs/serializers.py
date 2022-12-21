from rest_framework import serializers

from .models import Song
from albums.serializers import AlbumSerializer


class SongSerializer(serializers.ModelSerializer):
    # album = AlbumSerializer(read_only=True)
    class Meta:
        model=Song
        fields=["id", "title", "duration", "album_id"]
        
        
    def create(self, validated_data):
        return Song.objects.create(**validated_data)
