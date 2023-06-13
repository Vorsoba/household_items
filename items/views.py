from django.shortcuts import render, get_object_or_404
from .forms import ItemForm
from .models import Item


def items_detail(request, id):
    item = get_object_or_404(Item, id=id)
    item_form = ItemForm(instance=item)
    return render(request, 'items_detail.html', {'item': item, 'item_form': item_form})


'''def items_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'items_detail.html', {'item': item})'''
