# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.test import TestCase
from home.views import get_index


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def check_status_code_200(self):
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)

    def check_content(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html").content
        self.assertEqual(home_page.content, home_page_template_output)
