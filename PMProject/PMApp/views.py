from distutils.command.install import value
from urllib import request

from django.shortcuts import render

# Create your views here.
from .models import Task


def lst(request):
    t = Task.objects.all()
    lst_1 = []
    for i in t:
        lst_1.append({'Task', i})
        c = {'lst_1': lst_1}
    return render(request, "base.html", {'con': c})


def admin_object(request):
    x = Task.objects.all()
    Tasks = []
    for i in x:
        Tasks.append(i)

    return render(request, "base.html", {"Tasks": Tasks})
