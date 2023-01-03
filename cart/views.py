# Imports
# 3rd party:
from django.shortcuts import render

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
# ~~~~~~~~~~


def Cart(request):
    """
    cart page view
    """
    return render(request, "cart/cart.html")


def AddCart(request):
    """
    cart page view
    """
    return render(request, "cart/cart.html")
