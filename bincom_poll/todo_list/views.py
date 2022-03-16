from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import DatabaseError

# Create your views here.

from .models import Item


def index(request):
    items = Item.objects.all().order_by('status', '-id')
    return render(request, 'index.html', {'items': items})


def add(request):
    title = request.POST['title']
    description = request.POST['description']

    try:
        item = Item()
        item.title = title
        item.description = description
        item.save()
    except (Exception, DatabaseError) as e:
        # print(e)
        pass
    return HttpResponseRedirect('/')


def toggle(request, item_id):
    item = Item.objects.get(id=item_id)
    item.status = not item.status
    item.save()
    return HttpResponseRedirect('/')


def delete(request, item_id):
    Item.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/')
