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
from payup.models import Order
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Profile(View):
    """
    A class for the Orders History
    """
    def get(self, request, *args, **kwargs):
        """
        Get Product Detail Function
        """
        act_user = request.user
        queryset = Order.objects
        if request.user.is_superuser:
            orders = get_list_or_404(queryset)

        if get_list_or_404(queryset, owner=act_user):
            orders = get_list_or_404(queryset, owner=act_user)
        else:
            orders = get_object_or_404(queryset, owner=act_user)
        # , owner=act_user
        # Order.all()
        context = {
            "orders": orders,
            }
        return render(
            request,
            "userprofile/profile.html",
            context,
        )

