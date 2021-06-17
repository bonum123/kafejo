
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('user.urls')),
    path('api/v1/food/', include('food.urls')),
    path('api/v1/reviews/', include('review.urls')),
]
