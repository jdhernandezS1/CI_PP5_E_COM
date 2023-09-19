# Imports
# 3rd party:
from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
from e_comm.urls import router
# ~~~~~~~~~~

router.register(r'users', views.UsersView, 'todo')

urlpatterns = [
    path('', views.index, name='home'),
    path('about_us/', views.AboutUs, name='about_us'),
    path(
        'api/token/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path(
        'api/token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'
        )
]
