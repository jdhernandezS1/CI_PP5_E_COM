# Imports
# 3rd party:
from django.shortcuts import render, get_object_or_404
from django.shortcuts import reverse, get_list_or_404, redirect
from django.shortcuts import render
from django.contrib import messages
from django.views import generic, View
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
    messages.success(request, message)
    return redirect(redirect_url)


class RemoveCart(View):
    """
    Remove one product to the cart
    """
    def get(self, request, prod_id):
        cart = request.session.get('cart', {})
        if prod_id in list(cart.keys()) and cart[prod_id] > 0:
            cart[prod_id] = cart[prod_id]-1
            message = "Done"
            if cart[prod_id] == 0:
                cart.pop(prod_id)
        else:
            message = "The Product Is not in your cart"
        request.session['cart'] = cart
        messages.success(request, message)
        return redirect("cart")


class PlusCart(View):
    """
    Add one product of the cart
    """
    def get(self, request, prod_id):
        cart = request.session.get('cart', {})
        if prod_id in list(cart.keys()) and cart[prod_id] > 0:
            cart[prod_id] = cart[prod_id]+1
        else:
            message = "The Product Is not in your cart"
        message = "Done"
        request.session['cart'] = cart
        messages.success(request, message)
        return redirect("cart")
