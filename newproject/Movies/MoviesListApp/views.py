from django.shortcuts import render


import datetime

from inventory.models import Bee_hive

# Create your views here.
'''def index(request):
    return render(request,"base.html")
def Movie_Name(request):
   name = request.GET.get("name")
   return render(request, 'result.html', {"name": name})
'''





def Publisher_list(request):
    PublisherVar = Publisher.objects.all()
    Publisher_list =[]
    for item in PublisherVar:
        Publisher_list.append({'Publisher':item})

    context = {'Publisher_list': Publisher_list}
    return render(request,'MoviesListApp/base.html',context)