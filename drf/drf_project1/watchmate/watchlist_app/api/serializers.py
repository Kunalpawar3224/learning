from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    descritory = serializers.CharField()
    active_field = serializers.BooleanField()