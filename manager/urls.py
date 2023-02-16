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
        'del<int:productid>/',
        views.DelItem,
        name='del_item'
        ),
    path(
        'Add_Product/',
        views.AddItem,
        name='add_item'
        ),
    path(
        'edit<int:productid>/',
        views.EditItem,
        name='edit_item'
        ),
    path(
        'add_category/',
        views.AddCategory.as_view(),
        name='add_category'
        ),
    path(
        'edit_category/<int:id>/',
        views.EditCategory.as_view(),
        name='edit_category'
        ),
    path(
        'del/<int:id>/',
        views.DeleteCategory.as_view(),
        name='del_category'
        ),
]
