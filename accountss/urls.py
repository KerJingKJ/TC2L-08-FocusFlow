# accountss/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('homepage/', views.homepage, name='homepage'),
   
]

from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
