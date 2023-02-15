"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404
from django.shortcuts import reverse, get_list_or_404
from django.views import generic, View
from django.contrib import messages
from django.core.exceptions import ValidationError
# Internal
from .forms import ContactForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ContactUs(View):
    """
    A class for the Contact Us Page
    """
    def get(self, request, *args, **kwargs):
        """
        Get Function
        """
        template = "contact/contact_us.html"
        act_user = request.user
        form = ContactForm()
        context = {
            "act_user": act_user,
            "form": form,
            }
        return render(
            request,
            template,
            context,
        )
