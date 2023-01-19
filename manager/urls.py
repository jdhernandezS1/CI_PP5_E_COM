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
        views.ProductManager,
        name='products_manager'
    ),
    path(
        '<slug:title_slug>/',
        views.DelItem,
        name='del_item'
        ),
]
