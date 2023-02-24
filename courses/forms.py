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
from courses.models import Post, Comment
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
            'email',
            'body',
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email',
            'body': 'Body',
            }
        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}*'
            else:
                placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'manager-style-input'
            self.fields[field].label = None


class PostForm(forms.ModelForm):
    """
    A class for form to manage post
    """
    class Meta:
        """
        To order items
        """
        model = Post
        fields = (
            'title',
            'content',
            'featured_image',
            )
    featured_image = CloudinaryFileField(
        options={
            "folder": "posts/",
            'width': 531,
            'height': 531,
            }
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'content': 'Description',
            'featured_image': 'Post Image',
            }
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}*'
            else:
                placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'manager-style-input'
            self.fields[field].label = None
