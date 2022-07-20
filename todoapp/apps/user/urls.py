# Vendor
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

# Local
from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view({'post': 'create'}), name='login'),
]