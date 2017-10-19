"""
    Forms.py:
    This will handle user authenticationagainst our DB
"""
from django import forms
from django.contrib.auth.models import User


# This class will be responsible for handling the registration of a new user
class UserRegisterForm(forms.ModelForm):
    """
    password1: The users password to enter initially
    password2: The users password re-entered
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        """
        model: The user model
        fields: The fields we wish to provide the user with for registration/sign-up
        """
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password(self):
        """
        clean_password: Here we check if the second password matches the first password
        entered, if they do not match we return a validation error message to the user
        """
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Sorry, the passwords do not match!')
        return cd['password2']


# This class will be responsible for handling the user login
class UserLoginForm(forms.Form):
    """
    username: The users name input field
    password: The users password input field
    We use the widget here to display the passwords HTML input, it includes a
    type="password" attr
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
