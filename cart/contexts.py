# Imports
# 3rd party:
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal]
from products.models import Prod
# ~~~~~~~~~~


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    number = 0
    for prod_id, quantity in cart.items():
        product = get_object_or_404(Prod, pk=prod_id)
        total += quantity * product.price
        product_count += quantity
        temp_tot = product.price * quantity
        number += 1
        cart_items.append({
            'number': number,
            'prod_id': prod_id,
            'quantity': quantity,
            'product': product,
            'temp_tot': temp_tot,
        })
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    contexts = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return contexts
