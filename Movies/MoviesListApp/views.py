from django.shortcuts import render
from .models import Publisher


def publisher_list(request):
    publisher = Publisher.objects.all()
    publisher_list = []

    for publisher in publisher:
        publisher_list.append({'publisher': publisher})

    context = {'publisher_list': publisher_list}
    return render(request, 'base.html', context)
