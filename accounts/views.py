# -  *  - coding:utf-8 -  *  -
from __future__ import unicode_literals
from django.template.context_processors import csrf
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.models import User
from accounts.forms import UserRegisterForm, UserLoginForm, EditUserForm, EditProfileForm
from accounts.models import Profile

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('user_profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")
    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


# this method handles user registration
def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST or None)
        if user_form.is_valid():
            # Create a new 'User' object
            new_user = user_form.save(commit=False)
            # Set the password to the users chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # save the new User object
            new_user.save()
            # create the users profile
            profile = Profile.objects.create(user=new_user)
            # finally return the registered html page request
            return render(request, 'accounts/register_done.html',  {'new_user': new_user})
    else:
        # if the user is not registered we wish to display the registration html page
        user_form = UserRegisterForm()
    return render(request, 'accounts/register.html',  {'user_form': user_form})


# here we specify that login is required
# this method redirects the user to their profile page on successful login
@login_required
def user_profile(request):
    return render(request, 'accounts/profile.html', {'section': 'profile'})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = EditUserForm(instance=request.user, data=request.POST)
        profile_form = EditProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('user_profile')
        else:
            messages.error(request, 'Sorry, but there was an error updating your profile')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})
