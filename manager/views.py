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
from .forms import ProdForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def ProductManager(request):
    """
    Get Products Function
    """
    if request.user.is_superuser:
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
    else:
        return redirect("home")


def DelItem(request, productid):
    """
    A clas To Delete An Item
    """
    if request.user.is_superuser:
        model = Prod
        # productid = request.session.get('productid')
        product = get_object_or_404(model, id=productid)
        product.delete()
        messages.success(request, 'The Product Was Deleted as well')
        redirect('products_manager')
    else:
        redirect("home")


def AddItem(request):
    """
    A clas To Add an Item
    """
    if request.method == 'POST':
        messages.success(request, 'The Product Was Added as well')

    if request.user.is_superuser:
        model = Prod
        product_form = ProdForm()
        template = "manager/add_product.html"
        context = {
            'product_form': product_form,
            }
        return render(
            request,
            template,
            context
            )
    else:
        redirect("home")
