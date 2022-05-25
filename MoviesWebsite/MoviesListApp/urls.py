from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('search/', views.search, name='search'),
    path('l/'), views.publishers, name='publishers')
]