# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BlogPost

# Register your models here.


# Customise the admin area so we can display more fields
class BlogPostAdmin(admin.ModelAdmin):
    """
    list_display: specifies the fields we wish to display in the admin panel
    list_filter: lets us customise the sidebar filter
    prepopulated_fields: use our posttitle as the post slug
    raw_id_fields: set the users id key as a number
    date_hierarchy: helps search quickly using the dates bar
    search_fields: create a search bar so we can search the posts
    ordering: specifies the default ordering for the posts
    """
    list_display = ('post_title', 'slug', 'post_author', 'publish')
    list_filter = ('post_author', 'created_date', 'published_date')
    prepopulated_fields = {'slug': ('post_title',)}
    raw_id_fields = ('post_author',)
    date_hierarchy = 'published_date'
    search_fields = ('post_title', 'post_body')
    ordering = ['post_author', 'published_date']


# Register our BlogPost & BlogPostAdmin to the admin area.
admin.site.register(BlogPost, BlogPostAdmin)
