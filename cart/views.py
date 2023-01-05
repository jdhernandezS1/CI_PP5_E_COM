# Imports
# 3rd party:
from django.shortcuts import render, get_object_or_404
from django.shortcuts import reverse, get_list_or_404, redirect
from django.shortcuts import render
from django.contrib import messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
# ~~~~~~~~~~


def Cart(request):
    """
    cart page view
    """
    return render(request, "cart/cart.html")


def AddCart(request, prod_id):
    """
    Add product to the cart
    """
    message = "The Product Was Added to the cart"
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if prod_id in list(cart.keys()):
        cart[prod_id] += quantity
    else:
        cart[prod_id] = quantity

    request.session['cart'] = cart
    # print(request.session['cart'])
    messages.success(request, message)
    return redirect(redirect_url)
