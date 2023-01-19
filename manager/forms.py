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
    def __init__(self, *args, **kwargs):
        """
        Placeholders classes labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'category': 'Category',
            'title': 'Title',
            'title_slug':'Title system',
            'quantity': 'Quantity',
            'price': 'Price',
            'featured_image': 'Product Image',
            'scountbool': 'Scount',
            'scount': 'Amount of Scount',
            'description': 'Product Description',
            }
        self.fields['category'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}*'
            else:
                placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'manager-style-input'
            self.fields[field].label = False

# Cat
#     author
#     title
#     slug
#     featured_image
