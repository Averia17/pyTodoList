from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    all_items = TodoItem.objects.all()
    return render(request, 'index.html', {'all_items': all_items})


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')


def deleteTodo(request, todo_id):
    item = TodoItem.objects.get(id=todo_id)
    item.delete()
    return HttpResponseRedirect('/')


def editTodo(request, todo_id):
    item = TodoItem.objects.get(id=todo_id)
    if request.method == 'POST':
        item.content = request.POST['content']
        item.save()
        return HttpResponseRedirect('/')
    return render(request, 'edit.html', {'item': item})
