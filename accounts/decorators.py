from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import update_last_login


def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function


def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_function(request, *args, **kwargs)
            else:
                # if request.user.member.id.exists():
                #     var = request.user.member.name
                #     if var is None:
                #         return redirect('member-profile')
                # return redirect('member-profile')
                return redirect('user-home')
        return wrapper_function
    return decorator


# def update_first_login(sender, user, **kwargs):
#     if user.last_login is None:
#         # First time this user has logged in
#         kwargs['request'].session['first_login'] = True
#     # Update the last_login value as normal
#     update_last_login(sender, user, **kwargs)
#
#
# user_logged_in.disconnect(update_last_login)
# user_logged_in.connect(update_first_login)