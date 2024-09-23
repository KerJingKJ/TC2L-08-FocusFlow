

from django.urls import include,path
from . import views

urlpatterns = [
    path('log_mood/', views.log_mood, name='log_mood'),
    path('mood_history/', views.mood_history, name='mood_history'),
    path('mood/', views.mood, name='mood'),
    path('mood_history/', views.mood_history, name='mood_history'),
    path('', views.homepage, name='homepage'),
    path('workspace/', include('goals.urls')),

    
]
