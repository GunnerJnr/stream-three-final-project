# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import GamersHubProducts


# Create your views here.
@login_required(login_url='/login/')
def products_list(request):

    object_list = GamersHubProducts.objects.all.order_by('price')
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
