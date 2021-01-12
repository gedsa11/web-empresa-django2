from django.urls import path
from . import views #el punto . indica el directorio actual

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
]