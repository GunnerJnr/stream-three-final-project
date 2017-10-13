"""
    Forms.py:
    This will handle user authenticationagainst our DB
"""
from django import forms


class UserLoginForm(forms.Form):
    """
    username: The users name input field
    password: The users password input field
    We use the widget here to display the passwords HTML input, it includes a
    type="password" attr
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
