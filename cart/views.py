from django.shortcuts import render


def cart(request):
    """
    cart page view
    """
    return render(request, "cart/cart.html")
