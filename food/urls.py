from django.urls import path
from . import views

urlpatterns = [
    path('', views.FoodListView.as_view()),
    path('<int:pk>/', views.FoodDetailView.as_view()),
    path('categories/', views.CategoryView.as_view()),
    ]
