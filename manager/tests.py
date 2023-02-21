# Imports
# 3rd party:
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
from django.test import Client
from allauth.tests import Mock, TestCase, patch
from allauth.utils import get_user_model, get_username_max_length
from django.core.exceptions import ValidationError
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
    user.save()


def create_superuser(self):
    user = User.objects.create_superuser(
        username="test",
        email="test@mail.com",
        password="123test"
        )
    user.save()


class ProducsTests(TestCase):
    """
    Test Product Manager
    """
    def test_products_manager_view(self):
        """
        Test Products Manager View
        """
        user = create_superuser(self)
        self.client.login(
            username='test',
            password='123test'
            )
        url = reverse('products_manager')
        response = self.client.get(url, user)
        self.assertEqual(response.status_code, 200)

    def test_products_manager_view_no_admin(self):
        """
        test Products manager view as normal user
        """
        user = create_user(self)
        self.client.login(
            username='test',
            password='123test'
            )
        url = reverse('products_manager')
        with self.assertRaises(ValidationError):
            response = self.client.get(url, user)


class CatsTests(TestCase):
    """
    Test Views
    """
    def test_categories_manager_view(self):
        """
        test category manager view
        """
        user = create_superuser(self)
        self.client.login(
            username='test',
            password='123test'
            )
        url = reverse('cats_manager')
        response = self.client.get(url, user)

    def test_categories_manager_view_no_admin(self):
        """
        test category manager view
        """
        user = create_user(self)
        self.client.login(
            username='test',
            password='123test'
            )
        url = reverse('cats_manager')
        with self.assertRaises(ValidationError):
            response = self.client.get(url, user)

    def test_categories_add_view(self):
        """
        test add category view
        """
        user = create_superuser(self)
        self.client.login(
            username='test',
            password='123test'
            )
        url = reverse('add_category')
        response = self.client.get(
            url
            )
        self.assertEqual(response.status_code, 200)
