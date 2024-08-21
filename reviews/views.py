from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermissions
from reviews.models import Review
from reviews.serializer import ReviewSerializer


class ReviewListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailsUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissions,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
