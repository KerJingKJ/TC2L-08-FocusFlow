# moods/urls.py  
from django.urls import path  
from .views import mood_view  

urlpatterns = [  
    path('mood/', mood_view, name='mood'),  
]