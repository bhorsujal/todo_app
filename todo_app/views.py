from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def home_view(request):
    tasks = Todo.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def create_task_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description)
        return redirect('home')
    return redirect('home')

def update_task_view(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Todo, pk=pk)
        task.isCompleted = True
        task.save()
        return redirect('home')
    return redirect('home')

def delete_task_view(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Todo, pk=pk)
        task.delete()
        return redirect('home')
    return redirect('home')

def delete_all_tasks_view(request):
    if request.method == 'POST':
        Todo.objects.all().delete()
        return redirect('home')
    return redirect('home')

def update_task_details_view(request, pk):
    task = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        new_title = request.POST['title']
        new_description = request.POST['description']

        if new_title:
            task.title = new_title
        if new_description:
            task.description = new_description

        task.save()
        return redirect('home')

    # if not post request then render the update page with the current task details
    return render(request, 'update.html', {'task': task})