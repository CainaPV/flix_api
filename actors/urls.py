from django.urls import path
from . import views
urlpatterns = [
    path('actors/',views.ActorCreateList.as_view(), name = 'create-list-view' ),
    path('actors/<int:pk>/', views.ActorDetailsUpdateDelete.as_view(), name = 'details-update-delete-view'),
 ]