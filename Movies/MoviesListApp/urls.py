from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index_viwes),
    path('movies-search/', views.Search),
    path('Publisher_list/', views.Publisher_list, name='Publisher_list')
]
