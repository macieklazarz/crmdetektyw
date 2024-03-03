from django.contrib import admin
from django.urls import path, include
from .views import SprawaListView, SprawaDetailView
from django.contrib.auth import views

app_name = 'sprawy'




urlpatterns = [

    path('', SprawaListView.as_view(), name="case_list_view"),
    path('case_detail/<uuid:pk>/', SprawaDetailView.as_view(), name="case_detail"),

    ]