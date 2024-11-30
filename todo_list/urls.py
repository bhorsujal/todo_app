from django.contrib import admin
from django.urls import path, include
from todo_app.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo_app.urls')),
    path('', home_view, name='home'),
]