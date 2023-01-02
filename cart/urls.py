# Imports
# 3rd party:
from django.urls import path, include
from django.contrib import admin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
# ~~~~~~~~~~

urlpatterns = [
    path('', views.Cart, name='cart'),
    path('add/<prod_id>/', views.AddCart, name='add_to_cart'),

]
