from django.urls import path
from . import views

urlpatterns = [
               path('list_', views.Publisher, name='list_') ,

               ]