from django.shortcuts import render
from django.db.models import Avg
from movies.models import Movie
from genres.models import *
from reviews.models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermissions
from movies.serializer import MovieModelSerializer, MovieSerializerDinamic


class MovieListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalPermissions,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieSerializerDinamic
        return MovieModelSerializer



class MovieDetailsUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalPermissions,)
    queryset = Movie.objects.all()
    
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieSerializerDinamic
        return MovieModelSerializer
    

class MovieStatics(APIView):
    permission_classes = (IsAuthenticated,GlobalPermissions,)
    queryset = Movie.objects.all()
    

    def get(self, request):
        total_movies = self.queryset.count()
        list_genres = ({'name': g.name,'id': g.id} for g in Genre.objects.all())
        # list_genres_in_movies = self.queryset.values('genre__name', 'genre__id').distinct()
        total_reviews = Review.objects.count()
        total_rate_stars = Review.objects.aggregate(Avg('stars'))['stars__avg']


        return Response(data = {'total_movies': total_movies, 'list_genres': list_genres, 'total_reviews': total_reviews,'total_rate_stars': round(total_rate_stars,1)}, 
                        status= HTTP_200_OK,)
        

