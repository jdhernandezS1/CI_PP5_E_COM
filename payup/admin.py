"""
Imports
"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
# Internal
from .models import Order, OrdProd
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class OrderProds(admin.TabularInline):
    model = OrdProd
    readonly_fields = (
        'prods_total',
        )


class OrderAdmin(admin.ModelAdmin):
    inlines = (
        OrderProds,
        )

    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        )

    fields = (
        'order_number',
        'full_name',
        'email',
        'phone_number',
        'canton',
        'city',
        'postcode',
        'street_address1',
        'street_address2',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        )

    list_display = (
        'order_number',
        'date',
        'full_name',
        'order_total',
        'delivery_cost',
        'grand_total',
        )

    ordering = (
        '-date',
        '-order_number',
        )


admin.site.register(Order, OrderAdmin)
