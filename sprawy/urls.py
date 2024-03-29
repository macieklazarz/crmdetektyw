from django.contrib import admin
from django.urls import path, include
from .views import SprawaListView, SprawaDetailView, SprawaCreateView, CaseUpdateView, NotatkaUpdateView, BrudnopisUpdateView
from django.contrib.auth import views

app_name = 'sprawy'




urlpatterns = [

    path('', SprawaListView.as_view(), name="case_list_view"),
    path('case_detail/<uuid:pk>/', SprawaDetailView.as_view(), name="case_detail"),
    path('case_update/<uuid:pk>/', CaseUpdateView.as_view(), name="case_update"),
    path('case_new/', SprawaCreateView.as_view(), name="case_new"),
    path('note_update/<uuid:pk>/', NotatkaUpdateView.as_view(), name="note_update"),
    path('draft_update/<uuid:pk>/', BrudnopisUpdateView.as_view(), name="draft_update"),

    ]