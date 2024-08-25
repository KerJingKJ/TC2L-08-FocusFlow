# accountss/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),  # or some other view
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
]