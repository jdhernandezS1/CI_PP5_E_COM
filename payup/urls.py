# Imports
# 3rd party:
from django.urls import path, include
from django.contrib import admin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
# ~~~~~~~~~~

urlpatterns = [
    path(
        '',
        views.PayUp,
        name="pay"),
    path(
        'CheckDetails/<order_number>',
        views.PayUpCheck,
        name="check"),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name="cache_checkout_data"),
]

cache_checkout_data