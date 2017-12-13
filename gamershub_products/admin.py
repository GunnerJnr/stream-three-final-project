"""
Admin.py:
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import GamersHubProducts

# Register products to admin panel
admin.site.register(GamersHubProducts)
