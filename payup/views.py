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
from django.conf import settings
from cart.contexts import cart_contents
from .forms import OrderForm
from .models import OrdProd, Order
from products.models import Prod
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def PayUp(request):
    """
    Pay UP view
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'canton': request.POST['canton'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }

        order_form = OrderForm(form_data)
        print(order_form)
        if order_form.is_valid():
            order = order_form.save()
            for prod_id, quantity in cart.items():
                try:
                    product = Prod.objects.get(id=prod_id)
                    products_order = OrdProd(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    products_order.save()
                    messages.success(request, (
                        "Thank you For buy with us!")
                    )
                    # del request.session['cart']
                    # Solve error
                except Prod.DoesNotExist:
                    messages.error(request, (
                        "A product in your cart does not exists"
                        "Call us for help you!")
                    )
                    order.delete()
                    return redirect(reverse('cart'))

            request.session['save_info'] = 'save-info' in request.POST
            args = [order.order_number]
            # return redirect(reverse('checkout_success', args))
            return redirect(reverse('cart'))
        else:
            messages.error(request, 'An error has occurred. \
                Please check the information and try again.')

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty at the moment")
        return redirect(reverse('prods_cat'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Contact us and give the reference \
            Stripe public key is missing.')

    template = 'payup/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
