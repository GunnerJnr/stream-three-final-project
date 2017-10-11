# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import BlogPost


# Create your views here.

# define a view to return a list of our blog posts with the 'published' status
def blog_post_list(request):
    blog_posts = BlogPost.published.all()
    return render(request, 'gamersblog/blogpost/blogpostlist.html',
                           {'blog_posts', blog_posts})


# define a view that will return a single blog post
def blog_post_detail(request, day, month, year, blog_post):
    blog_post = get_object_or_404(BlogPost,
                                  slug=blog_post,
                                  status='published',
                                  publish__year=year,
                                  publish__month=month,
                                  publish__day=day)
    return render(request, 'gamersblog/blogpost/blogpostdetail.html')
