from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/', views.accounts, name="accounts"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/accounts.html'), name='login'),
    path('', views.accounts, name='account'),
    path('update/', views.update_profile, name='update_profile'),
    path('delete/', views.delete_account, name='delete_account'),
]


