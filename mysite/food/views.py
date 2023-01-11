from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView

from mysite.food.forms import ItemForm, UpdateItemForm
from mysite.food.models import Item


# function-base-view


# def index(request):
#     item_list = Item.objects.all()
#
#     context = {
#         'item_list': item_list
#     }
#     return render(request,'food/index.html',context)



# class-base-view

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'



def item(request):
    return HttpResponse('this is another vieuw')


# function-base-view

# def detail(request, item_id):
#     items = Item.objects.get(pk=item_id)
#
#     context = {
#         'item': items
#     }
#     return render(request, 'food/detail.html',context)


# class-base- view

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'



def create_item(request):
    form= ItemForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'food/item-form.html', context)


def update_item(request, item_id):
    items = Item.objects.get(id=item_id)
    if request.method == 'POST':
        form = UpdateItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = UpdateItemForm(instance=items)

    context = {
        'form': form,
        'items': items
    }
    return render(request, 'food/update-item-form.html', context)


def delete_item(request,item_id):
    items = Item.objects.get(id=item_id)
    if request.method =='POST':
        items.delete()
        return redirect('index')

    context = {
        'items':items
    }

    return render(request,'food/item-delete.html', context )