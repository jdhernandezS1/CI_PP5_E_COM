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


class Prod(models.Model):
    """
    A class for product model
    """
    category = models.ForeignKey(
        Cat,
        on_delete=models.CASCADE,
        related_name="category"
    )

    title = models.CharField(
        max_length=200,
        unique=True
        )

    title_slug = models.SlugField(
        max_length=200,
        unique=True
        )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
        )

    scount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
        )

    quantity = models.IntegerField(
        default=0
        )

    featured_image = CloudinaryField(
        'image',
        default='placeholder'
        )

    scountbool = models.BooleanField()

    description = models.TextField()

    created_on = models.DateTimeField(
        auto_now_add=True
        )

    class Meta:
        """
        Items Order
        """
        ordering = [
            '-created_on',
            'category',
            'title',
            ]

    def __str__(self):
        """
        Return Title
        """
        return str(self.title)
