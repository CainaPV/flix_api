from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
      model = Review
      fields = '__all__'

    def validate_comment(self, value):
      if len(value) > 30:
         raise serializers.ValidationError('Neste campo é permitido apenas 30 caracteres')
      return value