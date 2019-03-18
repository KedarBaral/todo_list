from django.shortcuts import render, redirect, get_object_or_404
from .models import List
from .forms import ListForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, 'Item has been added to list.')
            return render(request, 'todo/index.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'todo/index.html', {'all_items': all_items})


def delete(request, list_id):
    item = get_object_or_404(List, pk=list_id)
    item.delete()
    messages.success(request, 'Item has been deleted.')
    return redirect('todo:index')


def cross_off(request, list_id):
    item = get_object_or_404(List, pk=list_id)
    item.completed = True
    item.save()
    return redirect('todo:index')


def uncross(request, list_id):
    item = get_object_or_404(List, pk=list_id)
    item.completed = False
    item.save()
    return redirect('todo:index')


def edit(request, list_id):
    if request.method == "POST":
        item = get_object_or_404(List, pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Item has been edited.')
            return redirect('todo:index')

    else:
        item = get_object_or_404(List, pk=list_id)
        return render(request, 'todo/edit.html', {'item': item})

