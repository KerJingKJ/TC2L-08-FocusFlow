from django.urls import path
from . import views

urlpatterns = [
    path('goals/', views.goals, name="goals")
]