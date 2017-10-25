# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogPost


# define a view to return a list of our blog posts with the 'published' status
def blog_post_list(request):
    object_list = BlogPost.published.all()
    # add pagination to the blog page, we will display 4 posts per page
    paginator = Paginator(object_list, 4)  # 4 posts in each page
    page = request.GET.get('page')
    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        # if the page is not an integer deliver the first page
        blog_posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver the last page of results
        blog_posts = paginator.page(paginator.num_pages)
    return render(request, 'gamersblog/blogposts/blogpostlist.html', {'page': page, 'blog_posts': blog_posts})


# define a view that will return a single blog post
def blog_post_detail(request, day, month, year, post):
    post = get_object_or_404(BlogPost,
                             post_slug=post,
                             post_status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    post.post_views += 1  # increment the post views by 1, each time one is seen
    post.save()
    return render(request, 'gamersblog/blogposts/blogpostdetail.html', {'post': post})
