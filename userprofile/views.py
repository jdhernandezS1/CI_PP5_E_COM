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
from payup.models import Order
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Profile(View):
    """
    A class for the Orders History
    """
    def get(self, request, *args, **kwargs):
        """
        Get Order Detail Function
        """
        template = "userprofile/profile.html"
        act_user = request.user
        queryset = Order.objects
        if request.user.is_superuser:
            orders = get_list_or_404(queryset)
        else:
            orders = Order.objects.filter(owner=act_user)
        context = {
            "orders": orders,
            }
        return render(
            request,
            template,
            context,
        )
