from django.urls import path
from . import views

urlpatterns = [
    path('mood/', views.mood_view, name="mood")
]