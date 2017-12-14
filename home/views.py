"""
Views.py:
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# create a view to return the sites index page
def get_index(request):
    """
    get_index:
    """
    # returns the home view template
    return render(request, 'index.html')
