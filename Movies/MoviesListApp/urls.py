from django.urls import path
from . import views

urlpatterns = [
    path('', views.publisher_list, name='publisher_list')
]
