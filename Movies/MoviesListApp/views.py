from django.shortcuts import render
from .models import Publisher

def Index_viwes(request):
    return render(request,"base.html",)

def Search(request):
    word= request.GET.get('word')
    return render(request,"movies-search.html",{'word':word})

def Publisher_list(request):
    p = Publisher.objects.all()
    Publisher_list = []
    for i in p:
        Publisher_list.append({'Publisher': i})

    context = {'Publisher_list': Publisher_list}
    return render(request, 'Publisher_list.html', context)

