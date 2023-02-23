"""
Imports
"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Internal
from .models import Post, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin class For Post Model
    """
    list_display = (
        'title',
        'content',
        'featured_image',
        )
    search_fields = [
        'title',
        'created_on',
        ]
    list_filter = (
        'title',
        'created_on'
        )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin class For Comment Model
    """
    list_display = (
        'name',
        'email',
        'created_on'
        )
    search_fields = [
        'name'
        ]
    list_filter = (
        'name',
        'email',
        'created_on'
        )
