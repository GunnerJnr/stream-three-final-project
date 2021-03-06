"""
Views.py:
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import BlogPostForm
from .models import BlogPost


# define a new view to handle the creation of a new blog post
@login_required
def new_post(request):
    """
    new_post(request): handle the creation of a new blog post
    """
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        # if the form is valid
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.published_date = timezone.now()
            # check the post title is unique
            post_title = form.cleaned_data['post_title']
            # if the title exists throw an error
            if BlogPost.objects.filter(post_title__iexact=post_title).exists():
                # tell the user to pick a new title, this one exists
                form.add_error(None, 'Sorry that title already exists')
            else:
                # otherwise save the form
                post = form.save()
                # notify the user they were successful in adding a post
                form.add_error(None, 'Your post has been added successfully')
                # redirect the the blog post detail page
                return redirect('blog_post_detail', post.slug)
    else:
        form = BlogPostForm()
    # render the form for the user to create a blog post
    return render(request, 'gamersblog/blogposts/blogpostform.html', {'form': form})


# define a new view to handle the editing of a blog post
@login_required
def edit_post(request, slug):
    """
    edit_post(request, slug): responsible for handling the editing of a blog post
    """
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.published_date = timezone.now()
            post = form.save()
            return redirect('blog_post_detail', post.slug)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'gamersblog/blogposts/blogpostform.html', {'form': form})


# define a view to return a list of our blog posts with the 'published' status
def blog_post_list(request):
    """
    Create a view that will return a list of
    Posts that were published prior to 'now' and
    render them to the 'blogposts.html' template
    :param request:
    :return:
    """
    object_list = BlogPost.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    # add pagination to the blog page, we will display 3 posts per page
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        # if the page is not an integer deliver the first page
        blog_posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver the last page of results
        blog_posts = paginator.page(paginator.num_pages)
    return render(request, 'gamersblog/blogposts/blogpostlist.html',
                  {'page': page, 'blog_posts': blog_posts})


# define a view that will return a single blog post
def blog_post_detail(request, slug):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    post = get_object_or_404(BlogPost, slug=slug)
    post.post_views += 1  # increment the post views by 1, each time one is seen
    post.save()
    return render(request, 'gamersblog/blogposts/blogpostdetail.html', {'post': post})


# create a view to show the most viewd blog posts
def most_viewed(request):
    """
    we wnat to get and list the top five most popular
    blog posts and display them in blogpost.html on clicking the
    link in the navigation menu
    :param request:
    :return:
    """
    top_posts = BlogPost.objects.filter(
        published_date__lte=timezone.now()).order_by('-post_views')[:10]
    # add pagination to the blog page, we will display 3 posts per page
    paginator = Paginator(top_posts, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        # if the page is not an integer deliver the first page
        blog_posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver the last page of results
        blog_posts = paginator.page(paginator.num_pages)
    return render(request, 'gamersblog/blogposts/blogpostlist.html',
                  {'page': page, 'blog_posts': blog_posts})
