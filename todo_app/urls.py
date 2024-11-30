from django.urls import path
from . import views

urlpatterns = [
    # Specifying names to use in tests.py with reverse() function
    path('create/', views.create_task_view, name='todo-list'),
    path('update/<int:pk>/', views.update_task_view, name='todo-update'),
    path('delete/<int:pk>/', views.delete_task_view, name='todo-delete'),
    path('delete_all/', views.delete_all_tasks_view, name='todo-delete-all'),
    path('update_details/<int:pk>/', views.update_task_details_view, name='todo-update-details'),
]