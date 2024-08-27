from django.urls import path
from . import views

urlpatterns = [
    path('', views.mood_view, name="mood")
]