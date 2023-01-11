"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404
from django.shortcuts import reverse, get_list_or_404, redirect
from django.db.models import Q
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ValidationError
import stripe
# Internal
# from .models import
from .forms import OrderForm
import os
if os.path.isfile('env.py'):
    import env
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def PayUp(request):
    """
    Pay UP view
    """
    cart = request.session.get('cart',{})
    if not cart:
        messages.error(request, "Your cart is empty at the moment")
        return redirect(reverse('prods_cat'))

    template = "payup/checkout.html"
    orderform = OrderForm()
    public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    private_key = os.environ.get('STRIPE_SECRET_KEY')
    # 
    stripe.api_key = private_key
    intent = stripe.PaymentIntent.create(
    amount=1099,
    currency='chf',
    # Verify your integration in this guide by including this parameter
    metadata={'integration_check': 'accept_a_payment'},
    # 
)

    context = {
        'order_form': orderform,
        'stripe_public_key': public_key,
        'client_secret': private_key
    }
    return render(
        request,
        template,
        context
        )
