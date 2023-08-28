from django.shortcuts import render
from item.models import Item

ph_no = "+916006324328"

# Create your views here.
def myitems(request):

    
    items = Item.objects.all()
    context = {
        "items" : items,
        "ph" : ph_no
    }
    return render(request, 'item/myitems.html', context=context)

def food(request):


    items = Item.objects.filter(category__name = "food")
    context = {
        "items" : items,
        "ph" : ph_no
    }
    return render(request, 'item/myitems.html', context=context)

def toys(request):

    items = Item.objects.filter(category__name = "toys")
    context = {
        "items" : items,
        "ph" : ph_no
    }
    return render(request, 'item/myitems.html', context=context)

def accessories(request):

    items = Item.objects.filter(category__name = "accessories")
    context = {
        "items" : items,
        "ph" : ph_no
    }
    return render(request, 'item/myitems.html', context=context)