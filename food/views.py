from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from django.template import loader
from .forms import ItemForm

def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    #return HttpResponse(item_list)
    context = {
        'item_list': item_list,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse("This  is an item view.")

def info(request):
    return HttpResponse("I am loving this song called: Ngwa!")

def detail(request, item_id):
    item = Item.objects.get(pk = item_id)
    context = {
        'item' : item,
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    
    if (form.is_valid()):
        form.save()
        return redirect('food')
    
    return render(request, 'food/item-form.html', {'form': form})

 








