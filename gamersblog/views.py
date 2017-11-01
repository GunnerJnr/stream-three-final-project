# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogPost
from .forms import BlogPostForm


# define a new view to handle the creation of a new blog post
@login_required
def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST or None, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post_title = form.cleaned_data['post_title']
            if BlogPost.objects.filter(post_title=post_title).exists():
                messages.error(request, 'title already exists')
            else:
                post = form.save()
                messages.success(request, 'post added successfully')
            return redirect(post.get_absolute_url())
    else:
        form = BlogPostForm()
    return render(request, 'gamersblog/blogposts/blogpostform.html', {'form': form})


# define a view to return a list of our blog posts with the 'published' status
def blog_post_list(request):
    object_list = BlogPost.published.all()
    # add pagination to the blog page, we will display 6 posts per page
    paginator = Paginator(object_list, 6)  # 6 posts in each page
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
def blog_post_detail(request, day, month, year, pk, slug):
    post = get_object_or_404(BlogPost, post_slug=slug,
                             pk=pk,
                             post_status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    post.post_views += 1  # increment the post views by 1, each time one is seen
    post.save()
    return render(request, 'gamersblog/blogposts/blogpostdetail.html', {'post': post})
