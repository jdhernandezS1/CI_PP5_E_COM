from django.shortcuts import render
from django.views import generic, View

from products.models import Cat


class ServerDeniesAcces(View):
    """
    Page not found Error 403
    """
    def get(self, request, *args, **kwargs):
        template = 'errors/403.html'
        return render(request, template)


class PageNotFound(View):
    """
    Page not found Error 404
    """
    def get(self, request, *args, **kwargs):
        template = 'errors/404.html'
        return render(request, template)


class InternalServerError(View):
    """
    Page not found Error 500
    """
    def get(self, request, *args, **kwargs):
        template = 'errors/500.html'
        return render(request, template)
