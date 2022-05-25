# Create your views here.
from django.shortcuts import render
import models

# Create your views here.


def index(request):
    x = 'HELLO'
    return render(request, "index.html", {'x': x})

def Movie_Search(request):
    search = request.GET.get('search') or 33
    return render(request, "search.html", {'search': search})

def Publisher_List(request, val=None):
   plist= models.Publisher.objects.all()
   context = [{'key': val}]
   return render(request, "base2.html",context)