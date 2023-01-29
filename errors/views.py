"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.views import generic, View
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def ServerDeniesAcces(request, exception):
    template = 'errors/403.html'
    return render(request, template, status=403)


def PageNotFound(request, exception):
    template = 'errors/404.html'
    return render(request, template, status=404)


def InternalServerError(request, exception):
    template = 'errors/500.html'
    return render(request, template, status=500)


# def InternalServerError(request):
#     template = 'errors/500.html'
#     return render(request, template, status=500)
