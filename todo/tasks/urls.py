from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('index', views.index),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]


