from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from django.shortcuts import render

from main.models import Item

def show_main(request):
    products = Item.objects.all()

    context = {
        'name': 'Nazwa Arifah Ikhsan',
        'class': 'PBP E',
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
