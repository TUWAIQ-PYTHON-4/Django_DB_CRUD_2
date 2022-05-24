from django.urls import path
from django.contrib import admin
import PMApp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PMApp.views.admin_object)

]