"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Cat(models.Model):
    """
    A class for Category product model
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="prod"
        )
    title = models.CharField(
        max_length=200,
        unique=True
        )
    slug = models.SlugField(
        max_length=200,
        unique=True
        )
    featured_image = CloudinaryField(
        'image',
        default='placeholder'
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )

    class Meta:
        """
        Items Order
        """
        ordering = [
            '-created_on'
            ]

    def __str__(self):
        """
        Return Title
        """
        return str(self.title)


# class product(models.Model):
#     """
#     A class for product model
#     """
#     content = models.TextField()
#     featured_image = CloudinaryField(
#         'image',
#         default='placeholder'
#         )
