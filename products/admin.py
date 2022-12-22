"""
Imports
"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Internal
# Register your models here.
from .models import Cat,  Prod
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    """
    Post model class For posts in Blog
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
    Post model class For Product
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
