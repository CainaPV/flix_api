from django.urls import path
from . import views
urlpatterns = [   
    path('genres/', views.GenreCreateList.as_view(), name='create-list-view'),
    path('genres/<int:pk>/', views.GenreDetailsUpdateDelete.as_view(), name= 'details-update-delete-view' ),
]