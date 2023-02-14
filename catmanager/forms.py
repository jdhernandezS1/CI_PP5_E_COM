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


class CategoryForm(forms.ModelForm):
    """
    A class for form to create a category
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
            'featured_image'
        )

    def __init__(self, *args, **kwargs):
        """
        Placeholders classes labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'author': 'Author',
            'title': 'Title',
            'slug': 'Slug',
            'featured_image': 'Featured_image',
            }
        self.fields['Title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}*'
            else:
                placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'manager-style-input'
            self.fields[field].label = None
