from django.conf.urls import url
from accounts import views as accounts_views

urlpatterns = [
    # accounts app URLs
    url(r'^login/$', accounts_views.user_login, name='login'),
]
