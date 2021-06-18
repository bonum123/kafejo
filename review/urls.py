from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewApiView.as_view()),
    # path('<int:pk>', views.ReviewRetrieveView.as_view()),
]