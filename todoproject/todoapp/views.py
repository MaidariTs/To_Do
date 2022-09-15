from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import ToDoListItem


URL = '/todoapp/'


def ToDoAppView(request):
    all_todo_items = ToDoListItem.objects.all()
    return render(request, 'todolist.html',
                  {'all_items': all_todo_items})


def AddToDoView(request):
    x = request.POST['content']
    if x == '':
        return HttpResponseRedirect(URL)
    else:
        new_item = ToDoListItem(content=x)
        new_item.save()
        return HttpResponseRedirect(URL)


def DeleteToDoView(request, i):
    y = ToDoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect(URL)
