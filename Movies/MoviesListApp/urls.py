from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies_search/', views.movies_search, name='movies_search'),
    path('Publisher_list/', views.Publisher_list, name='Publisher_list')
]
