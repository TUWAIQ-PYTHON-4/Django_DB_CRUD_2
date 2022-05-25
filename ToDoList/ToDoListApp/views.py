from django.shortcuts import render
from .models import AboutModel
from .forms import AboutForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):

    context = {}
    form = AboutForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request,'about.html', context)

