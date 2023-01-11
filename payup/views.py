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
# from flask import Flask, render_template, jsonify, request
# Internal
# from .models import
from cart.contexts import cart_contents
from .forms import OrderForm
import os
if os.path.isfile('env.py'):
    import env
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def PayUp(request):
    """
    Pay UP view
    """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty at the moment")
        return redirect(reverse('prods_cat'))

    template = "payup/checkout.html"
    orderform = OrderForm()
    public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    private_key = os.environ.get('STRIPE_SECRET_KEY')
    #
    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = private_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency='chf',
        # Verify your integration in this guide by including this parameter
        metadata={'integration_check': 'accept_a_payment'},
    )

    if not public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    context = {
        'order_form': orderform,
        'public_key': public_key,
        'client_secret': intent.client_secret,
    }
    return render(
        request,
        template,
        context
        )
