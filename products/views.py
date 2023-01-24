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
# Internal
from .models import Cat, Prod
from .forms import CommentForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def ProdSearch(request):
    """
    A view to search products
    """
    products = Prod.objects.all()
    message = "Please write a key word"
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.success(request, message)
                return redirect(reverse('prods_cat'))
            q1 = Q(title__icontains=query)
            q2 = Q(description__icontains=query)
            queries = q1 | q2
            prod_list = products.filter(queries)
    context = {
        'prod_list': prod_list,
        'search_term': query,
    }
    return render(
        request,
        'products/products.html',
        context
        )

    # prod_list


def ProdCat(request):
    """
    Get Products Function to get in order
    """
    prod_list = Prod.objects.all()
    orders = None
    categories = None
    if request.GET:
        if 'categ' in request.GET:
            categories = str(request.GET['categ'])
            categories = get_object_or_404(Cat, title=categories).id
            prod_list = get_list_or_404(prod_list, category=categories)

        if 'order' in request.GET:
            orders = request.GET['order']
            queryset = prod_list.order_by(orders)
            prod_list = get_list_or_404(queryset)
    context = {
                "prod_list": prod_list,
                "categories": categories,
                "orders": orders
                # "form": Form()
            }
    return render(
        request,
        "products/products.html",
        context
        )


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
        comments = prod.comments.order_by('created_on')
        context = {
            "comments": comments,
            "prod": prod,
            "comment_form": CommentForm(),
            "prodid": prod.title_slug,
            }
        return render(
            request,
            "products/prod_detail.html",
            context,
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Post function to comment
        """
        prod = get_object_or_404(Prod, title_slug=slug)
        comments = prod.comments
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user.username
            comment = comment_form.save(commit=False)
            comment.producup = prod
            comment.save()
        else:
            comment_form = CommentForm()
            raise ValidationError(
                    "The Content is not valid"
                )
        context = {
                "comments": comments,
                "comment_form": comment_form,
                "prodslug": prod.title_slug,
                "prodid": prod,
            }
        messages.success(request, 'Your comment was sent')
        return redirect('prods_cat')