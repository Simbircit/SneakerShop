from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import logout


def main(request):

    sneakers = Sneakers.objects.all()
    firms = Firm.objects.all()
    cart_items = CartItem.objects.filter(user=request.user.id)
    total_price = sum(item.sneakers.price * item.quantity for item in cart_items)

    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        order = Order()
        order.user = User.objects.get(username=request.user.username)
        order.price = total_price
        order.order_info = f"{cart_items}"
        order.save()
        cart = cart_items
        order.cart.set(cart)

        return HttpResponseRedirect('/clear_cart/')

    else:
        form = Order()
    context = {'sneakers': sneakers, 'firms': firms, 'cart_items': cart_items, 'form': form, 'total_price': total_price}

    return render(request, 'shapp/main.html', context)


def main_filtered(request, firm_name):

    sneakers = Sneakers.objects.filter(firm__name=firm_name)
    firms = Firm.objects.all()
    cart_items = CartItem.objects.filter(user=request.user.id)
    total_price = sum(item.sneakers.price * item.quantity for item in cart_items)

    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        order = Order()
        order.user = User.objects.get(username=request.user.username)
        order.price = total_price
        order.order_info = f"{cart_items}"
        order.save()
        cart = cart_items
        order.cart.set(cart)

        return HttpResponseRedirect('/clear_cart/')

    else:
        form = Order()

    context = {'sneakers': sneakers, 'firms': firms, 'cart_items': cart_items, 'form': form, 'total_price': total_price}

    return render(request, 'shapp/main.html', context)


def product(request, sneakers_id):

    sneakers = Sneakers.objects.get(id=sneakers_id)
    cart_items = CartItem.objects.filter(user=request.user.id)
    total_price = sum(item.sneakers.price * item.quantity for item in cart_items)

    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        order = Order()
        order.user = User.objects.get(username=request.user.username)
        order.price = total_price
        order.order_info = f"{cart_items}"
        order.save()
        cart = cart_items
        order.cart.set(cart)

        return HttpResponseRedirect('/clear_cart/')

    else:
        form = Order()

    context = {'sneakers': sneakers, 'cart_items': cart_items, 'form': form, 'total_price': total_price}

    return render(request, 'shapp/sneakers.html', context)


def add_to_cart(request, sneakers_id):

    sneakers = Sneakers.objects.get(id=sneakers_id)
    cart_item, created = CartItem.objects.get_or_create(sneakers=sneakers, user=request.user)

    cart_item.quantity += 1
    cart_item.save()
    return redirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, item_id):

    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def remove_one_from_cart(request, item_id):

    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity += -1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect(request.META.get('HTTP_REFERER'))


def clear_cart(request):

    cart_item = CartItem.objects.filter(user=request.user)
    for i in cart_item:
        i.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def register(request):

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:

        form = CreateUser

    return render(request, 'shapp/register.html', {'form': form})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
