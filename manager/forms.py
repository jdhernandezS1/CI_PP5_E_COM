"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from products.models import Cat, Prod


class ProdForm(forms.ModelForm):
    """
    A class for form to create a meal
    """
    class Meta:
        """
        To order items
        """
        model = Prod
        fields = (
            'category',
            'title',
            'title_slug',
            'quantity',
            'price',
            'featured_image',
            'scountbool',
            'scount',
            'description'
            )

# Cat
#     author
#     title
#     slug
#     featured_image
