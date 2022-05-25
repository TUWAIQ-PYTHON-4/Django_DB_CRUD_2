from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.Movie_Search, name='Movie_Search'),
    path(r'^$', views.Publisher_List, name='Publisher_List')

]
