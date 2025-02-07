from rest_framework import serializers

from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    descritory = serializers.CharField()
    active_field = serializers.BooleanField()


    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.descritory = validated_data.get('descritory', instance.descritory)
        instance.active_field = validated_data.get('active_field', instance.active_field)
        instance.save()
        return instance