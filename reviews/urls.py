from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewListCreate.as_view(), name= 'list-create-view'),
    path('reviews/<int:pk>/', views.ReviewDetailsUpdateDelete.as_view(), name= 'details-update-delete-view')
    ]