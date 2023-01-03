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
        'result/',
        views.ProdSearch,
        name='s_prods'
        ),
    path(
        '',
        views.ProdCat,
        name='prods_cat'
    ),
    path(
        'prods/<slug:slug>/',
        views.ProdDetail.as_view(),
        name="prod_detail"),
]
