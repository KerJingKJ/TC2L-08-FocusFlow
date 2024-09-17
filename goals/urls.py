from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.set_goals, name="set_goals"),
    path('edit/<int:goal_id>', views.edit, name='edit'),
    path('delete/<int:goal_id>', views.delete, name='delete'),
    path('complete/<int:goal_id>/<str:action>', views.complete, name='complete'),
    # path('goals/', views.goals, name='goals')
    path('timer/', views.timer_view, name='timer'),  # Partial timer view
    path('timer/pause/', views.timer_pause, name='timer_pause'),
]


