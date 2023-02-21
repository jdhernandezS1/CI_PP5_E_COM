# Imports
# 3rd party:
from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render
from django.test import Client
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ViewsTests(TestCase):
    """
    Test Views
    """
    def test_404_view(self):
        """
        page 404 test
        """
        url = '/home404/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
