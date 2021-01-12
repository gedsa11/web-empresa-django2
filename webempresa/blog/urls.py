from django.urls import path
from . import views #el punto . indica el directorio actual

urlpatterns = [
    path('', views.blog, name="blog"),  
    path('category/<int:category_id>/', views.category, name="category"),
]