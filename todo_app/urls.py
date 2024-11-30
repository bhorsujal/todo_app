from django.urls import path
from .views import TodoListView, TodoDetailView, TodoDeleteAllView

urlpatterns = [
    # Specifying names to use in tests.py with reverse() function
    path('todos/', TodoListView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todos/delete_all/', TodoDeleteAllView.as_view(), name='todo-delete-all'),
]