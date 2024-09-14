

from django.urls import path
from . import views

urlpatterns = [
    path('log_mood/', views.log_mood, name='log_mood'),
    path('mood_history/', views.mood_history, name='mood_history'),
    path('mood/', views.mood, name='mood'),
    path('mood_tracking/', views.mood_tracking, name='mood_tracking_view'),
    path('mood_history/', views.mood_history, name='mood_history'),


    
]
