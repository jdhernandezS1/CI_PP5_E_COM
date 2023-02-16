"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
from cloudinary.forms import CloudinaryFileField
from django_summernote.fields import SummernoteTextFormField
from django_summernote.fields import SummernoteTextField
# Internal
from products.models import Cat, Prod
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class CatForm(forms.ModelForm):
    """
    A class for form to manage a Category
    """
    class Meta:
        """
        To order items
        """
        model = Cat
        fields = (
            'author',
            'title',
            'slug',
            )


class ProdForm(forms.ModelForm):
    """
    A class for form to create a Product
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
    featured_image = CloudinaryFileField(
            options={
                "folder": "products/",
                'width': 531,
                'height': 531,
                }
            )

    def __init__(self, *args, **kwargs):
        """
        Placeholders classes labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'category': 'Category',
            'title': 'Title',
            'title_slug': 'System Title',
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
            if field == 'scountbool':
                self.fields[field].label = "Article in Scount"
            else:
                self.fields[field].label = None
