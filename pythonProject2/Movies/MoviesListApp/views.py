from .models import Publisher
from django.shortcuts import render


# Create your views here.

def list_(request):
    list_ = Publisher.objects.all()
    context = {'list_': list_}
    return render(request, 'list_/base.html', context)
