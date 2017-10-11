# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BlogPost

# Register your models here.


# Customise the admin area so we can display more fields
class BlogPostAdmin(admin.ModelAdmin):
    """
    list_display: specifies the fields we wish to display in the admin panel
    prepopulated_fields: use our posttitle as the post slug
    raw_id_fields: set the users id key as a number
    date_hierarchy: helps search quickly using the dates bar
    search_fields: create a search bar so we can search the posts
    ordering: specifies the default ordering for the posts
    """
    list_display = ('post_title', 'post_slug', 'post_author', 'publish',
                    'post_status')
    list_filter = ('post_status', 'created_date', 'publish', 'post_author')
    prepopulated_fields = {'post_slug': ('post_title',)}
    raw_id_fields = ('post_author',)
    date_hierarchy = 'publish'
    search_fields = ('post_title', 'post_body')
    ordering = ['post_status', 'publish']


# Register our BlogPost & BlogPostAdmin to the admin area.
admin.site.register(BlogPost, BlogPostAdmin)
