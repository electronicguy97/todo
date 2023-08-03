from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        task = Task(title=title)
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_add.html')

def task_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')
