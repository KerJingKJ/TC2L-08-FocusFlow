from django.urls import path
from . import views

urlpatterns = [
    path('countdown/', views.countdown, name="countdown")
]