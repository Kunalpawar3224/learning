from rest_framework import serializers

from watchlist_app.models import Movie


def name_length( value):
    if len(value) < 3: 
         raise serializers.ValidationError('Name must be at least 3 characters long.')
        # else:
        #     return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
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
    
    def validate(self, data):
        if data['name'] == data['descritory']:
            raise serializers.ValidationError('Name and Description cannot be same.')
        else:
            return data
        
    #Field lvele validation
    # def validate_name(self, value):
    #     if len(value) < 3: 
    #         raise serializers.ValidationError('Name must be at least 3 characters long.')
    #     else:
    #         return value