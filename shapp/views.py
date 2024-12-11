from django.shortcuts import render, redirect
from .models import *
from .forms import *


def main(request):

    sneakers = Sneakers.objects.all()
    firms = Firm.objects.all()
    cart_items = CartItem.objects.all()
    context = {'sneakers': sneakers, 'firms': firms, 'cart_items': cart_items}

    return render(request, 'shapp/main.html', context)


def main_filtered(request, firm_name):

    sneakers = Sneakers.objects.filter(firm__name=firm_name)
    firms = Firm.objects.all()
    cart_items = CartItem.objects.all()
    context = {'sneakers': sneakers, 'firms': firms, 'cart_items': cart_items}

    return render(request, 'shapp/main.html', context)


def add_to_cart(request, sneakers_id):

    sneakers = Sneakers.objects.get(id=sneakers_id)
    cart_item, created = CartItem.objects.get_or_create(sneakers=sneakers)

    cart_item.quantity += 1
    cart_item.save()
    return redirect('/')


def remove_from_cart(request, item_id):

    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('/')
