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
    """
    Server Access Denied Error
    """
    template = '403.html'
    return render(request, template, status=403)


def PageNotFound(request, exception):
    """
    Page Not Found Error
    """
    template = '404.html'
    return render(request, template, status=404)


def InternalServerError(request, exception):
    """
    Internal Server Error
    """
    template = '500.html'
    return render(request, template, status=500)
