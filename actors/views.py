from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermissions
from actors.models import Actor
from actors.serializer import ActorSerializer

class ActorCreateList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalPermissions,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorDetailsUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalPermissions,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer 
