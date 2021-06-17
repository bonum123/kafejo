from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from . import serializers
from .models import Food, Category
from django_filters import rest_framework as filters
from django.db import connection
from django.db.models import Q

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class FoodListView(generics.ListAPIView):
    queryset = Food.objects.all()
    # queryset = Food.objects.select_related('category')
    serializer_class = serializers.FoodSerializer
    filters_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('title', 'price', 'category')
    pagination_class = StandardResultsSetPagination

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        print(f'Queries Counted: {len(connection.queries)}')
        return response

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', '')
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(id__icontains=search) | Q(price__icontains=search))
        return queryset





class FoodDetailView(generics.RetrieveAPIView):
    """Endpoint for retrieve single post"""
    queryset = Food.objects.all()
    serializer_class = serializers.FoodDetailSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer