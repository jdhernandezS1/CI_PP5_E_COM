"""
Imports
"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin
# Internal
# Register your models here.
from .models import Cat
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    """
    Post model class For posts in Blog
    """
    list_display = ('title', 'slug', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    list_filter = ('title', 'created_on')
