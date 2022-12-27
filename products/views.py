"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render,  get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ValidationError
# Internal
from .models import Cat, Prod
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProdList(generic.ListView):
    """
    A class for the products ordered by "created on"
    """
    model = Prod
    queryset = Prod.objects.all().order_by('-created_on')
    template_name = 'products/products.html'
    paginate_by = 6


class ProdDetail(View):
    """
    A class for the product details ordered by "created on"
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Get Product Detail Function
        """
        queryset = Prod.objects
        prod = get_object_or_404(queryset, title_slug=slug)
        # title_slug
        context = {
                "prod": prod
                # "comment_form": CommentForm()
            }
        return render(
            request,
            "products/prod_detail.html",
            context,
        )
