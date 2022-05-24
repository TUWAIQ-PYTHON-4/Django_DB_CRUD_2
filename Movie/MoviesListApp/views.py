from django.shortcuts import render
from .models import Publisher


def Publisher_list(request):
    PublisherVar = Publisher.objects.all()
    Publisher_list =[]
    for item in PublisherVar:
        Publisher_list.append({'Publisher':item})

    context = {'Publisher_list': Publisher_list}
    return render(request,'MoviesListApp/Publisher_list.html',context)