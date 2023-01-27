"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
from django.conf.urls import handler404, handler500
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path('403', views.ServerDeniesAcces, name='403'),
    path('404', views.PageNotFound, name='404'),
    path('500', views.InternalServerError, name='500'),
]

handler500 = views.InternalServerError
