from django.shortcuts import render, get_object_or_404

from MoviesListApp import models
from MoviesListApp.models import Publisher


def index(request):
    context= models.Publisher.objects.all()
    return render(request, 'base.html', {'context':context})


def search(request):
    search = request.GET.get('search')

    return render(request, 'search.html', {'search': search})

# def Publisher_list(self):
#    for self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher']):

#     return Publisher.objects.filter(publisher=self.publisher)
