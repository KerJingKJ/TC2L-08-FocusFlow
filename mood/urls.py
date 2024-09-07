from django.urls import path
from . import views

urlpatterns = [
    path('', views.mood_view, name="mood"),
    path('mood_tracking/', views.mood_tracking, name='mood_tracking'),
   
]
