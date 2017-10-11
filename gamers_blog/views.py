# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import BlogPost


# Create your views here.

# define a view to return a list of our blog posts with the 'published' status
def blog_post_list(request):
    blog_posts = BlogPost.published.all()
    return render(request, 'gamers_blog/blog_post/blog_post_list.html',
                           {'blog_posts', blog_posts})
