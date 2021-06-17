from rest_framework import generics, permissions
from review import serializers
from review.models import Review, Mark


class ReviewApiView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ReviewRetrieveView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class MarkApiView(generics.ListAPIView):
    queryset = Mark.objects.all()
    serializer_class = serializers.MarkSerializer
