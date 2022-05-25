from django.shortcuts import render, get_object_or_404

from MoviesListApp.models import Publisher


def index(request):
    return render(request, 'base.html')


def search(request):
    search = request.GET.get('search')

    return render(request, 'search.html', {'search': search})


 def Publisher_list(self):
     self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
     return Publisher.objects.filter(publisher=self.publisher)
