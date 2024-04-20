from django.contrib import admin
from django.urls import path
import my_project.views

urlpatterns = [
    path('', my_project.views.index),
]
