from django.conf.urls import url
from . import views as gamersblog_views

urlpatterns = [
    # gamersblog post views
    url(r'^$', gamersblog_views.blog_post_list, name='blog_post_list'),

    # we use regex here, we say the day and month need 2 digits,
    # and the year needs 4 digits, also the post can be words or hyphens
    url(r'^(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})/' r'(?P<post>[-\w]+)/$', gamersblog_views.blog_post_detail, name='blog_post_detail'),
    url(r'^post/new/$', gamersblog_views.new_post, name='new_post'),
]
