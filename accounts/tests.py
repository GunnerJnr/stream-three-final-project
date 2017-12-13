"""
Tests.py:
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from accounts.forms import *  # import all forms, pylint: disable=W0401, W0614,

# Create our test class
class SetUpClass(TestCase):
    """
    SetUpClass(TestCase):
        Set Up the User Class
    """

    def setUp(self):
        self.user = User.objects.create(
            username='exampleTestUser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            password='adminroot123',
            )

class UserFormTest(TestCase):
    """
    UserFormTest(TestCase):
        Handles the Tests for the register and login forms
    """
    def test_form_is_valid(self):
        """
        test_form_is_valid(self):
            Checks if the form data is valid
        """
        form = UserRegisterForm(data={
            'username': 'exampleTestUser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'adminroot123',
            'password2': 'adminroot123'
            })
        self.assertTrue(form.is_valid())


    def test_form_is_invalid(self):
        """
        test_form_is_invalid(self):
            Checks if the form data is invalid
        """
        form = UserRegisterForm(data={
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': '',
            'password2': ''
            })
        self.assertFalse(form.is_valid())


    def test_user_registration(self):
        """
        test_user_registration(self):
            Test the user registration form
        """
        user_register = self.client.post('accounts/register', {
            'username': 'exampleTestUser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'adminroot123',
            'password2': 'adminroot123'
        })
        self.assertTrue(user_register)


    def test_username_login(self):
        """
        test_user_login(self):
            Test the user login using the users chosen username
        """
        login_with_username = self.client.post('accounts/login.html', {
            'username': 'exampleTestUser',
            'password1': 'adminroot123',
            'password2': 'adminroot123'
        })
        self.assertTrue(login_with_username)


    def test_email_login(self):
        """
        test_user_login(self):
            Test the user login using the users email address
        """
        login_with_email = self.client.post('accounts/login.html', {
            'username': 'exampleuser@example.com',
            'password1': 'adminroot123',
            'password2': 'adminroot123'
        })
        self.assertTrue(login_with_email)
