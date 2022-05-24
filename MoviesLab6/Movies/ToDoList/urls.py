from django.urls import path
import ToDoList.views


urlpatterns = [
    path('', ToDoList.views.base),
    path('home/', ToDoList.views.home_view, name = 'hhome'),
    path('about/', ToDoList.views.about_view, name = 'aabout'),
    path('publisher_list/', ToDoList.views.publisher_list, name = 'pub')

]