from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.MovieListCreate.as_view(),name = 'create-list-view'),
    path('movies/<int:pk>/', views.MovieDetailsUpdateDelete.as_view(), name = 'details-update-delete-view'),
    path('movies/statics/', views.MovieStatics.as_view(), name='movie-statics'),
]