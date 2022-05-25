from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "base.html")


def movie_search(request):
    search= request.GET.get("search") or "Noura"
    return render(request, "search_movie.html", {"search":search})
