from django.urls import path
from . import views
import MoviesListApp

urlpatterns = [
    path('', MoviesListApp.views.index, name='index'),
    path('movie_search/', views.movie_search,name='movie_search')

]

