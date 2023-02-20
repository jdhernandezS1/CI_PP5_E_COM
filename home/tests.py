# Imports
# 3rd party:
from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
# ~~~~~~~~~~


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

    def test_404_view(self):
        """
        page 404 test
        """
        response = self.client.get(views.index)
        self.assertEqual(response.status_code, 404)

    def test_about_us_view(self):
        """
        page about us test
        """
        url = reverse('about_us')
        response = self.client.get(url)
        confirmation = self.assertEqual(response.status_code, 200)
