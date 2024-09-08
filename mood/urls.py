from django.urls import path
from . import views

urlpatterns = [
    path('', views.mood_list, name="mood"),
    path('mood_tracking/', views.mood_tracking, name='mood_tracking'),
    path('log_mood/', views.mood_list, name='log_mood'),
    path('mood_history/', views.mood_history, name='mood_history'),
    path('mood/', views.mood_list, name='mood_list'),
]
