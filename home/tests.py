# Imports
# 3rd party:
from django.urls import reverse
from django.shortcuts import render
from django.test import Client
from allauth.tests import Mock, TestCase, patch
from allauth.utils import get_user_model, get_username_max_length
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
# ~~~~~~~~~~


def create_user(self):
    user = get_user_model().objects.create(
        username="@test",
        is_superuser=True,
        password="123test"
        )
    user.save()
    return user


class ViewsTests(TestCase):
    """
    Test Views
    """
    def test_index_view(self):
        """
        testing home
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_us_view(self):
        """
        page about us test
        """
        url = reverse('about_us')
        response = self.client.get(url)
        confirmation = self.assertEqual(response.status_code, 200)


class UserTests(TestCase):
    """
    Test Views
    """
    def test_log_in(self):
        """
        test view
        """
        c = self.client
        response = c.post(
            '/accounts/login/',
            {'username': 'test', 'password': '123test'}
            )
        response = response.status_code

    def test_log_out(self):
        """
        test view
        """
        user = create_user(self)
        url = reverse('home')
        self.client.force_login(user)
        response = self.client.post(url)
