# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import GamersHubProducts


# Create your views here.
def all_products(request):
    products = GamersHubProducts.objects.all()
    return render(request, "products/products.html", {"products": products})
