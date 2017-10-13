# -  *  - coding:utf-8 -  *  -
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from accounts.forms import UserLoginForm


# Create your views here.
# Create a view to handle the users login.
def user_login(request):
    """
    UserLoginForm():
         We initialise the submitted data with our form login request,
    form.is_valid():
        we also check if the data entered is valid, if not return the
        errors to the user.
    user is not None:
        If the data is valid we check it against the db
         and return success.
    user.is_active:
        We also check if the users status is active or disabled and
        return a message.
    HttpResponse():
        We then log into the site if is_active is True.
    """
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],  password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('You have logged in successfully.')
                else:
                    return HttpResponse('This account is disabled, Sorry about that.')
            else:
                return HttpResponse('Invalid login, somethings not right')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html',  {'form': form})
