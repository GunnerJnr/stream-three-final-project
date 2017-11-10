# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import GamersHubProducts


# Create your views here.
@login_required(login_url='/login/')
def all_products(request):
    products = GamersHubProducts.objects.all()
    return render(request, "products/products.html", {"products": products})
