from django.conf.urls import puplisher, url

from . import views

urlpatterns = [
    path('', views.Publisher_list,name ='Publisher_list'),
]