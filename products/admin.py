"""
Imports
"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Internal
# Register your models here.
from .models import Cat,  Prod, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    """
    Admin model class For category
    """
    list_display = (
        'title',
        'slug',
        'created_on'
        )
    prepopulated_fields = {
        'slug': ('title',)
        }
    search_fields = [
        'title'
        ]
    list_filter = (
        'title',
        'created_on'
        )


@admin.register(Prod)
class ProdAdmin(SummernoteModelAdmin):
    """
    admin model class For Product
    """
    list_display = (
        'title',
        'title_slug',
        'scount'
        )
    prepopulated_fields = {
        'title_slug': ('title',)
        }
    search_fields = [
        'title',
        'title_slug'

        ]
    list_filter = (
        'title',
        'title_slug',
        'scount'
        )

    summernote_filds = ('description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Post model class For posts in Blog
    """
    list_display = (
        'producup',
        'created_on'
        )
    search_fields = [
        'name'
        ]
    list_filter = (
        'created_on',
        )
