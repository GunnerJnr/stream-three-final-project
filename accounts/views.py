# -  *  - coding:utf-8 -  *  -
from __future__ import unicode_literals
# from django.contrib.auth import views
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new 'User' object
            new_user = user_form.save(commit=False)
            # Set the password to the users chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # save the new User object
            new_user.save()
            # finally return the registered html page request
            return render(request, 'accounts/register_done.html',  {'new_user': new_user})
    else:
        # if the user is not registered we wish to display the registration html page
        user_form = UserRegisterForm()
    return render(request, 'accounts/register.html',  {'user_form': user_form})


@login_required
def user_profile(request):
    return render(request, 'accounts/profile.html',  {'section': 'profile'})
