from django.shortcuts import render
from genres.models import Genre
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermissions
from genres.serializer import GenreSerializer


class GenreCreateList(ListCreateAPIView):
  permission_classes = (IsAuthenticated,GlobalPermissions,)
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer


class GenreDetailsUpdateDelete(RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,GlobalPermissions,)
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer



 
       
