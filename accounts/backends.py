# -*- coding: utf-8 -*-
from django.contrib.auth.models import User


# Create your backends here.
class EmailAuth(object):
    """
    Authenticate the users using an email address
    """
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            raise None

    def get_user(self, user_id):
        """
        Used by the django authentication system to retrieve an instance of User
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
