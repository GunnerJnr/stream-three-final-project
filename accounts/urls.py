from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views


# accounts app URLs
urlpatterns = [
    # views using the built in django authentication - see link for reference
    # https://docs.djangoproject.com/en/1.11/topics/auth/default/#module-django.contrib.auth.views

    # django login views
    # https://docs.djangoproject.com/en/1.11/topics/auth/default/#how-to-log-a-user-in
    url(r'^login/$', auth_views.login, name='login'),

    # django logout views
    # https://docs.djangoproject.com/en/1.11/topics/auth/default/#how-to-log-a-user-out
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout-then-login', auth_views.logout_then_login, name='logout_then_login'),

    # change password views
    # https://docs.djangoproject.com/en/1.11/topics/auth/default/#changing-passwords
    url(r'^password-change/$', auth_views.password_change, name='password_change'),
    url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),

    # https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.PasswordResetView
    # password reset views
    url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),

    # Please see the below for the password_reset_email.html
    # https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.PasswordResetView

    # custom user views
    # accounts/profile views
    url(r'^$', accounts_views.user_profile, name='user_profile'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^edit-profile/$', accounts_views.edit, name='edit-profile'),
]
