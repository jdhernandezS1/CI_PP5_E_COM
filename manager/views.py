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
from .forms import ProdForm, CatForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class AddCategory(View):
    """
    A class for the Contact Us Page
    """
    def get(self, request, *args, **kwargs):
        """
        Get Function
        """
        template = "manager/add_category.html"
        form = CatForm()
        context = {
            "form": form,
            }
        return render(
            request,
            template,
            context,
        )

    def post(self, request, *args, **kwargs):
        """
        POST Function
        """
        form_data = {
            'author': request.POST['author'],
            'title': request.POST['title'],
            }
        form_data['slug'] = slugify(request.POST['title'])
        form = CatForm(form_data)

        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            redirect("products_manager")
        else:
            messages.error(request, 'An error has occurred. \
                    Please check the information and try again.')
            redirect("home")



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
        raise ValidationError(
            "The content is not valid or you do not\
                    have the permiss to do this"
            )
        return redirect("home")


def DelItem(request, productid):
    """
    A clas To Delete An Item
    """
    if request.method == 'GET':

        if request.user.is_superuser:
            model = Prod
            # productid = request.session.get('productid')
            product = get_object_or_404(model, id=productid)
            product.delete()
            messages.success(request, 'The Product Was Deleted as well')
            return redirect('products_manager')
        else:
            raise ValidationError(
                "The content is not valid or you do not\
                     have the permiss to do this"
                )
            return redirect("home")


def AddItem(request):
    """
    Add Item View
    """
    if request.method == 'POST':
        if request.user.is_superuser:

            form_data = {
                'category': request.POST['category'],
                'title': request.POST['title'],
                'quantity': request.POST['quantity'],
                'price': request.POST['price'],
                'scount': request.POST['scount'],
                'description': request.POST['description'],
            }
            # producto = get_object_or_404(Prod, title_slug='')
            # print(producto.featured_image)
            title = slugify(request.POST['title'])
            form_data['title_slug'] = slugify(request.POST['title'])
            prod_form = ProdForm(form_data, request.FILES)
            if prod_form.is_valid():
                product = prod_form.save(commit=False)
                product.save()
                return redirect('products_manager')
            else:
                messages.error(request, 'An error has occurred. \
                    Please check the information and try again.')
        else:
            raise ValidationError(
                "The content is not valid or you do not\
                     have the permiss to do this"
                )
            redirect("home")

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
        raise ValidationError(
            "The content is not valid or you do not\
                have the permiss to do this"
            )
        redirect("home")


def EditItem(request, productid):
    """
    A clas To edit Item
    """
    if request.method == 'POST':
        if request.user.is_superuser:
            form_data = {
                'category': request.POST['category'],
                'title': request.POST['title'],
                'quantity': request.POST['quantity'],
                'price': request.POST['price'],
                'scount': request.POST['scount'],
                'description': request.POST['description'],
            }
            title = slugify(request.POST['title'])
            form_data['title_slug'] = slugify(request.POST['title'])
            producto = get_object_or_404(Prod, id=productid)
            ref = get_object_or_404(Prod, id=productid)
            prod_form = ProdForm(form_data, request.FILES, instance=ref)
            if prod_form.is_valid():
                product = prod_form.save(commit=False)
                product.save()
                return redirect('products_manager')
            else:
                messages.error(request, 'An error has occurred. \
                    Please check the information and try again.')
        else:
            raise ValidationError(
                "The content is not valid or you do not\
                     have the permiss to do this"
                )
            redirect("home")
    # Get Response
    if request.user.is_superuser:
        model = Prod
        ref = get_object_or_404(Prod, id=productid)
        product_form = ProdForm(instance=ref)
        template = "manager/edit_product.html"
        context = {
            'productid': productid,
            'product_form': product_form,
            "product": ref,
            }
        return render(
            request,
            template,
            context
            )
    else:
        raise ValidationError(
            "The content is not valid or you do not\
                 have the permiss to do this"
            )
        redirect("home")
