from django.shortcuts import render
from .models import Task
def admin_object(request):
    x = Task.object.all()
    Task =[]
    for i in x:
        Task.append({i})
        return render(request, "base.html", {"Task":Task})