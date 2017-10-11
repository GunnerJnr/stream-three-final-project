# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BlogPost

# Register your models here.


# Customise the admin area so we can display more fields
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_slug', 'post_author', 'publish',
                    'post_status')


# Register our BlogPost & BlogPostAdmin to the admin area.
admin.site.register(BlogPost)
