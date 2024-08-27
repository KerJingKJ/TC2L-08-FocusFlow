from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_goals, name="set_goals"),
    path('edit/<int:goal_id>', views.edit, name='edit'),
    path('delete/<int:goal_id>', views.delete, name='delete')
]

