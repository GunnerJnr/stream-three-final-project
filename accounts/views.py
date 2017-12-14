"""
Views.py:
"""
# -  *  - coding:utf-8 -  *  -
from __future__ import unicode_literals

from accounts.forms import EditProfileForm, EditUserForm, UserRegisterForm
from accounts.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


# this method handles user registration
def register(request):
    """
    register: this view is responsible for registering a new user to the site
    """
    # if the request method is equal to POST
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST or None)
        # if the users form is valid
        if user_form.is_valid():
            # Create a new 'User' object
            new_user = user_form.save(commit=False)
            # Set the password to the users chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # save the new User object
            new_user.save()
            # create the users profile
            profile = Profile.objects.create(user=new_user)  # pylint: disable=W0612
            # finally return the register completed html page request
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        # if the user is not registered we wish to display the registration html page
        user_form = UserRegisterForm()
    # render the user form
    return render(request, 'accounts/register.html', {'user_form': user_form})


# here we specify that login is required
# this method redirects the user to their profile page on successful login
@login_required
def user_profile(request):
    """
    user_profile: this view is responsible for rendering the users profile page
    """
    # render the users profile page
    return render(request, 'accounts/profile.html', {'section': 'profile'})


@login_required
def edit(request):
    """
    edit: this view is seposnsible for editing the users profile page
    """
    # if the request method is equal to POST
    if request.method == 'POST':
        user_form = EditUserForm(instance=request.user, data=request.POST)
        profile_form = EditProfileForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES
                                      )
        # if the user form and the profile form are both valid
        if user_form.is_valid() and profile_form.is_valid():
            # save the user form
            user_form.save()
            # save the profile form
            profile_form.save()
            # give the user a message telling them their profile was updated successfully
            messages.success(request, 'Profile updated successfully')
            # return the user to their profile page
            return redirect('user_profile')
        else:
            # otherwise we throw the user an error message telling them we could not update
            # their profile page, and they need to fix the relevant field
            messages.error(
                request, 'Sorry, but there was an error updating your profile')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)
    # render the user form and profile form
    return render(request, 'accounts/edit_profile.html',
                  {'user_form': user_form,
                   'profile_form': profile_form
                  })
