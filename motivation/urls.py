from django.urls import path
from . import views

urlpatterns = [
    path('motivation/', views.motivation, name="motivation")
]