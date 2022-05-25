from django.shortcuts import render
from .models import Publisher


def index_view(request):
    return render(request, "base.html")


def search(request):
    search_word = request.GET.get("search_word") or "Harry potter"
    return render(request, "search.html", {"search_word": search_word})


def publishers(request):
    name = Publisher.objects.all()
    lst = []
    for i in lst:
        lst.append({'publisher name': name})
    return render(request, 'base.html', {'list': lst})
