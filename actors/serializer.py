from rest_framework import serializers
from actors.models import Actor

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'
       
    def validate_age(self, value):
        if value is not None and value > 105:
            raise serializers.ValidationError('Na atualidade não existi ator com esta idade')
        else:
            return value
         
class ActorSerializerActor(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['id', 'name']

        

