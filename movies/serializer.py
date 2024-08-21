from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie
from genres.models import Genre
from genres.serializer import GenreSerializer
from actors.serializer import ActorSerializer, ActorSerializerActor
from actors.models import Actor

#SERIALIZER.SERIALIZER
# class MovieSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(queryset = Genre.objects.all() )
#     realese_date = serializers.DateField()
#     actor = serializers.PrimaryKeyRelatedField(queryset= Actor.objects.all(), many= True)
#     resume = serializers.CharField()


#SERIALIZER.MODELSERIALIZER
class MovieModelSerializer(serializers.ModelSerializer):
    
    realese_date = serializers.DateField(format='%d/%m/%Y', input_formats=['%d/%m/%Y'])

    rate = serializers.SerializerMethodField(read_only=True) 

    class Meta:
        model = Movie
        fields = '__all__'
        

    def get_rate(self,obj):
      rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
      if rate:
         return round(rate,1)
      else:
         return 0  

    def validate_title(self, value):
       if len(value) > 50:
          raise serializers.ValidationError('Neste campo é permitido apenas 25 caracteres')
       else:
          return value   

    def validate_realese_date(self,value):
        if value.year < 2000:
         raise serializers.ValidationError('Só são permitidos filmes lançados a partir do ano 2000 em diante')
        else:
           return value

    def validate_resume(self, value):
       if len(value) > 60:
          raise serializers.ValidationError('Neste campo é permitido apenas 60 caracteres, escreva apenas os pontos marcantes e importantes do filme')
       else:
          return value


#SERIALIZER DINÂMICO (SEM ESTÁ NO PADRÃO RESTFUL)
class MovieSerializerDinamic(serializers.ModelSerializer):
   realese_date = serializers.DateField(format='%d/%m/%Y', input_formats=['%d/%m/%Y'])
   rate = serializers.SerializerMethodField(read_only = True)
   genre = GenreSerializer()
   actor = ActorSerializerActor(many = True)

   class Meta:
      model = Movie
      fields = ['rate', 'id', 'title', 'genre', 'actor', 'realese_date', 'resume']

   def get_rate(self, obj):
      rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
      if rate:
         return round(rate,1)
      else:
         return None 

      