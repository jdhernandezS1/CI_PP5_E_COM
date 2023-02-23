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


class Post(models.Model):
    """
    A class for Post model
    """
    title = models.CharField(
        max_length=200,
        unique=True
        )
    content = models.TextField()
    featured_image = CloudinaryField(
        'image',
        default='placeholder'
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    likes = models.ManyToManyField(
        User,
        related_name='post_likes',
        blank=True
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

    def number_of_likes(self):
        """
        Likes Counter
        """
        return self.likes.count()


class Comment(models.Model):
    """
    A class for Comment Model
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    name = models.CharField(
        max_length=80
        )
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True
        )

    class Meta:
        """
        Items Order
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment{self.body} by {self.name}"
