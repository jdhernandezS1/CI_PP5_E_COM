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
from products.models import Cat, Prod, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class CommentForm(forms.ModelForm):
    """
    A class for form to create a Comment
    """
    class Meta:
        """
        To order items
        """
        model = Comment
        fields = (
            'name',
            'email',
            'body',
            )
