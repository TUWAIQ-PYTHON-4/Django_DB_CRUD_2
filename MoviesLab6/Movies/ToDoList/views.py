from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render



def base(request):

    return render(request, "base.html")


def home_view(request):

    return render(request, "home.html")


def about_view(request):
    context = {'f_name': 'Mohammed', 'l_name': 'Sulaiman'}
    return render(request, "about.html", context)



list1 = ['Mohammed', 'Khalled']
list2 = ['https://mohammed.com', 'https://khalled.com']
list3 = ['moahmmed@pub.com', 'khalled@pub.com']

def publisher_list(request):

    context = {'publisher_name': " - ".join(list1)  ,'publisher_website': " - ".join(list2) ,'publisher_email': " - ".join(list3)}

    return render(request, "publisher_list.html", context)





