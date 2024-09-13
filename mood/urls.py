from django.urls import path
from . import views

urlpatterns = [
 #   path('', views.mood_list, name="mood"),
 #   path('mood_tracking/', views.mood_tracking, name='mood_tracking'),
 #   path('log_mood/', views.log_mood, name='log_mood'),
 #   path('mood_history/', views.mood_history, name='mood_history'),
 #   path('mood/', views.mood_list, name='mood_list'),
 #   path('mood/tracking/', views.mood_tracking, name='mood_tracking'),
 #   path('mood/create/', views.mood_create, name='mood_create'),
 #   path('mood/history/', views.mood_history, name='mood_history'),
  #  path('mood/log/', views.log_mood, name='log_mood'),
 #   path('mood/', views.mood, name='mood'),
 #   path('mood/list/', views.mood_list, name='mood_list'),

    path('', views.mood_list, name="mood"),
    path('mood_tracking/', views.mood_tracking, name='mood_tracking'),
    path('log_mood/', views.log_mood, name='log_mood'),
    path('mood_history/', views.mood_history, name='mood_history'),
    path('mood/create/', views.mood_create, name='mood_create'),
    path('mood_list/', views.mood_list, name='mood_list'),
]


