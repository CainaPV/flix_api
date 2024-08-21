from rest_framework import serializers
from genres.models import Genre

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
       

    def validate_name(self, value):
        if len(value) > 25:
            raise serializers.ValidationError('Neste campo é permitido apenas 25 caracteres')
        else:
            return value
