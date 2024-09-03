# accountss/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.homepage, name="homepage"),  # added trailing slash
    #path('logout/', views.logout_view, name='logout'),
    #path('profile/', views.ProfileView.as_view(), name='profile'),
     path('profile/', views.profile, name='profile'),
    path('password_change/', views.password_change, name='password_change'),
    path('logout/', views.logout_view, name='logout'),
]