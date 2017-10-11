# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.

# create a view to return the sites index page
def get_index(request):
    return render(request, 'index.html')
