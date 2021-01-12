from django.urls import path
from . import views #el punto . indica el directorio actual

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
]