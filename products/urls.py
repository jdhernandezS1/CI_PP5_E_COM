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
        views.ProdList.as_view(),
        name='prods'
        ),
    path(
        'result/',
        views.ProdSearch,
        name='s_prods'
        ),
    path(
        'cat/',
        views.ProdCat,
        name='prods_cat'
    ),
    path(
        'prods/<slug:slug>/',
        views.ProdDetail.as_view(),
        name="prod_detail"),
]
