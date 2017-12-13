"""
Tests.py:
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.test import TestCase
from home.views import get_index


class HomePageTest(TestCase):
    """
    HomePageTest(TestCase):
    """
    def test_home_page_resolves(self):
        """
        test_home_page_resolves(self):
        """
        # feed djangos test server our url to the homepage
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def check_status_code_200(self):
        """
        check_status_code_200(self):
        """
        # check the status code returns 200
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)

    def check_content(self):
        """
        check_content(self):
        """
        # check page content is OK
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html").content
        self.assertEqual(home_page.content, home_page_template_output)
