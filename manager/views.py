"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.shortcuts import reverse, get_list_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ValidationError
# Internal
from products.models import Cat, Prod
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def ProductManager(request):
    """
    Get Products Function
    """
    prod_list = Prod.objects.all()
    categories = Cat.objects.all()
    template = "manager/prods_manager.html"
    if request.GET:
        orders = 'title'
        queryset = prod_list.order_by(orders)
        prod_list = get_list_or_404(queryset)
    context = {
        "prod_list": prod_list,
        "categories": categories
        }
    return render(
        request,
        template,
        context
        )
