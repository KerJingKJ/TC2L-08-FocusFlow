# accountss/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('password_change/', views.password_change, name='password_change'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name="homepage"),
    
]

