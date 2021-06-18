from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from . import serializers
from .models import Food, Category


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class FoodListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = serializers.FoodSerializer
    pagination_class = StandardResultsSetPagination


class FoodDetailView(generics.RetrieveAPIView):
    """Endpoint for retrieve single post"""
    queryset = Food.objects.all()
    serializer_class = serializers.FoodDetailSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer