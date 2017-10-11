# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.

# Create our own custom manager, this will allow us to query our data
# using our own custom filter ('published') in this case.
class PublishedBlogPostManager(models.Manager):
    """
    get_queryset(): Override the defaultdjango queryset
    so we can apply a custom filter when calling queries.
    """

    def get_queryset(self):
        return super(PublishedBlogPostManager, self).get_queryset()\
                                                    .filter(post_status='published')


# Create the main class to handle our BlogPosts
class BlogPost(models.Model):
    """
    post_title: The blog post title.
    post_slug: Generates a slug for cleaner URLS (good for SEO).
    post_author: The blog post author (creates foreign key).
    post_body: The main body/content of the blog post.
    published_date: States when the post was published.
    created_date: The date the post was created.
    updated_date: States the date/time the post was last updated.
    post_status: Returns the status, meaning is it in draft or published state.

    We also added a unique_for_date field to our slug so this will be appended
    to the URL, this just helps to keep it unique.
    """

    # here we give the user a choice for saving their post as a draft or
    # publishing it right away.
    STATUS_CHOICES = (
        ('save_draft', 'Draft'),
        ('published', 'Published'),
    )

    # Create our settings that will be used in our blog posts.
    post_title = models.CharField(max_length=250)
    post_slug = models.SlugField(max_length=250, unique_for_date='publish')
    post_author = models.ForeignKey(User, related_name='blog_posts')
    post_body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    post_status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    # define our objects
    objects = models.Manager()  # default Django Manager
    published = PublishedBlogPostManager()  # Our Custom Manager

    class Meta:
        """
        post_order: Here we want to sort the blog posts, in this instance we
        chose descending order, we can easily use ascending by choosing:
        (e.g. 'publish').
        """
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('gamersblog:blog_post_detail',
                       args=[self.publish.strftime('%d'),
                             self.publish.strftime('%m'),
                             self.publish.year,
                             self.post_slug])

    def __unicode__(self):
        return self.title
