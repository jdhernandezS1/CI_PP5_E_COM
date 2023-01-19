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


class DelItem(generic.ListView):
    """
    A clas To Delete Item
    """
    model = Prod

    def post(self, request, title_slug, productid, **kwargs):
        """
        method To Delete Item
        """
        product = get_object_or_404(model, id=productid)
        product.delete()
        messages.success(request, 'The Product Was Deleted as well')
        return redirect('products_manager', title_slug)