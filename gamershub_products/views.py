"""
Views.py: -
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .models import GamersHubProducts


# Create your views here.
@login_required
def products_list(request):
    """
    products_list:
        Handles the pagination for the products to be displayed
    """
    object_list = GamersHubProducts.objects.get_queryset().order_by('id')
    # add pagination to the blog page, we will display 3 posts per page
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # if the page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver the last page of results
        products = paginator.page(paginator.num_pages)
    return render(request, 'products/products.html', {'page': page, 'products': products})
