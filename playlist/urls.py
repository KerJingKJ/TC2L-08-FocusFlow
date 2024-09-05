from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_playlist, name="select_playlist"),
   ]