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
        views.Cart,
        name='cart'
        ),
    path(
        'add/<prod_id>/',
        views.AddCart,
        name='add_to_cart'
        ),
    path(
        'minus/<prod_id>/',
        views.RemoveCart.as_view(),
        name='remove_one_cart'
        ),
    path(
        'plus/<prod_id>/',
        views.PlusCart.as_view(),
        name='add_one_cart'
        ),
]
