"""gamershub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from .settings import MEDIA_ROOT
from paypal.standard.ipn import urls as paypal_urls
from home import views as home_views
from gamershub_store import views as gamershub_paypal_views
from gamershub_products import views as gamershub_product_views

urlpatterns = [
    # add the url to access the admin panel
    url(r'^admin/', include(admin.site.urls), name='admin'),

    # accounts app urls
    url(r'^accounts/', include('accounts.urls')),

    # home app urls
    url(r'^$', home_views.get_index, name='home'),

    # here we want to add the urls from gamersblog app
    url(r'^blog/', include('gamersblog.urls')),

    # gamershub store urls
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', gamershub_paypal_views.paypal_return),
    url(r'^paypal-cancel', gamershub_paypal_views.paypal_cancel),

    # gamershub products urls
    url(r'^products/$', gamershub_product_views.all_products, name='products'),

    # Media Root urls
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
