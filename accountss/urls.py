# accountss/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.homepage, name="homepage"), 
    path('profile/', views.profile, name='profile'),
    path('password_change/', views.password_change, name='password_change'),
    path('logout/', views.logout_view, name='logout'),
    path('profile_display/', views.profile_display, name='profile_display'),
    path('password_change_done/', views.password_change_done, name='password_change_done'),

]

