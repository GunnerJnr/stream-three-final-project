from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views


# accounts app URLs
urlpatterns = [
    # django login views
    url(r'^login/$', auth_views.login, name='login'),

    # accounts/profile views
    url(r'^$', accounts_views.user_profile, name='user_profile'),

    # django logout views
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout-then-login', auth_views.logout_then_login, name='logout_then_login'),

    # change password views
    url(r'^password-change/$', auth_views.password_change, name='password_change'),
    url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
]
