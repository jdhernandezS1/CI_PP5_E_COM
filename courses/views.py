# Imports
# 3rd party:
from django.shortcuts import render, get_object_or_404
from django.shortcuts import reverse, get_list_or_404, redirect
from django.shortcuts import render
from django.contrib import messages
from django.views import generic, View
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
# ~~~~~~~~~~


class Courses(View):
    """
    Courses Views
    """
    def get(self, request, prod_id):
        return redirect("cart")
