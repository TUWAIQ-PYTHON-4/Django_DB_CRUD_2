from django.urls import path
from . import views

urlpatterns = [
    path('', views.Publisher_list,name ='Publisher_list'),
]
