from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login
from accounts import views as accounts_views

urlpatterns = [
    # accounts app URLs
    # django login views
    url(r'^login/$', login, name='login'),
    # accounts/profile views
    url(r'^$', accounts_views.user_profile, name='user_profile'),
    # django logout views
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login', logout_then_login, name='logout_then_login'),
]
