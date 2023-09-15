# Imports
# 3rd party:
from django.urls import path, include
from django.contrib import admin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
from e_comm.urls import router
# ~~~~~~~~~~
router.register(r'products', views.ProductsView, 'products')

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
