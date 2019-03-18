from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('todo/', include("todo.urls")),
]
