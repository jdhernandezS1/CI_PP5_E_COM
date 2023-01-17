# Imports
# 3rd party:
from django.urls import path, include
from django.contrib import admin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
from .webhook import webhook
# ~~~~~~~~~~

urlpatterns = [
    path(
        '',
        views.PayUp,
        name="pay"
        ),
    path(
        'CheckDetails/<order_number>',
        views.PayUpCheck,
        name="check"
        ),
    path(
        'cache_checkout_data/',
        views.Cache_Checkout_Data,
        name="cache_checkout_data"
        ),
    path(
        'wh/',
        webhook,
        name="webhook"
        ),
]
