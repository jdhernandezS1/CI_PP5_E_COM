"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.shortcuts import reverse, get_list_or_404, redirect
from django.views import generic, View
from django import forms
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from cloudinary.forms import cl_init_js_callbacks
import cloudinary
from django.core.exceptions import ValidationError
# Internal
from products.models import Cat, Prod
from .forms import CategoryForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def CategoryManager(request):
    """
    Get Products Function
    """
    if request.user.is_superuser:
        categories = Cat.objects.all()
        template = "catmanager/category_manager.html"
        if request.GET:
            orders = 'title'
            queryset = categories.order_by(orders)
            categories = get_list_or_404(queryset)
        context = {
            "categories": categories
            }
        return render(
            request,
            template,
            context
            )
    else:
        return redirect("home")
