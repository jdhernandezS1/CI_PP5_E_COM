# Imports
# 3rd party:
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render
from django.test import Client
from allauth.tests import Mock, TestCase, patch
from allauth.utils import get_user_model, get_username_max_length
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def create_user(self):
    user = get_user_model().objects.create(
        username="test",
        is_superuser=True,
        password="123test"
        )
    # user.set_password("test123")
    user.save()


def create_superuser(self):
    user = User.objects.create_superuser(
        username="test",
        email="test@mail.com",
        password="123test"
        )
    # user.set_password("test123")
    user.save()


class ViewsTests(TestCase):
    """
    Test Views
    """
    def test_products_manager_view(self):
        """
        test view
        """
        user = create_superuser(self)
        self.client.login(username='test', password='123test')
        url = reverse('products_manager')
        response = self.client.get(url, user)
