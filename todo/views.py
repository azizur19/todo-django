# Create your views here.
from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('description')
        Task.objects.create(title=title, description=desc)
        return redirect('/')
    return render(request, 'todo/index.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('/')
