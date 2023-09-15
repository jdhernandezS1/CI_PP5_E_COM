# Imports
# 3rd party:
from django.urls import path, include
from django.contrib import admin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
from e_comm.urls import router
# ~~~~~~~~~~

router.register(r'users', views.UsersView, 'todo')

urlpatterns = [
    path('', views.index, name='home'),
    path('about_us/', views.AboutUs, name='about_us'),

]
