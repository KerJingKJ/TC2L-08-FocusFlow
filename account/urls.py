# account\urls.py # 

#from django.contrib.auth import views as auth_views
# from . import views
# from django.urls import path, include

# urlpatterns = [
 #    path('account/', views.account, name="account"),
   #  path('', views.account, name='account'),
   # path('login/', auth_views.LoginView.as_view(template_name='account/account.html'), name='login'),
   # path('update/', views.update_profile, name='update_profile'),
   # path('delete/', views.delete_account, name='delete_account'),

   # path('', include("account.urls")),
#]


from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns = [
    path('', views.account, name='account'), # Handles /account/
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'), # Handles /account/login/
    path('update/', views.update_profile, name='update_profile'), # Handles /account/update/
    path('delete/', views.delete_account, name='delete_account'), # Handles /account/delete/
    # Removed the duplicate path definition
]