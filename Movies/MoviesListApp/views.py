from django.http import HttpResponse
from django.shortcuts import render
from .models import Publisher
# Create your views here.


"""def hello(request):
    m = "Hello"
    return HttpResponse(m)"""


# Task one
def index(request):
    x = "Rahaf"
    return render(request, 'base.html', {"x": x})


# Task Two
def movies_search(request):
    name = request.GET.get("name") or "Rahaf"
    return render(request, 'movies-search.html', {"name": name})


def Publisher_list(request):
    publisher = Publisher.objects.all()
    Publisher_list = []
    for Publishers in publisher:
        Publisher_list.append({'publisher': Publishers})

    context = {'Publisher_list': Publisher_list}
    return render(request, 'Publisher_list.html', context)


"""def name(request):
    x = request.GET.get("Rahaf")
    return HttpResponse("Hello {}".format(x))"""
