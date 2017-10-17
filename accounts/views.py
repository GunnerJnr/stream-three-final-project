# -  *  - coding:utf-8 -  *  -
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def user_profile(request):
    return render(request, 'accounts/profile.html', {'section': 'profile'})
