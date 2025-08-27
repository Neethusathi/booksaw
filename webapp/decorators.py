from django.shortcuts import redirect
from functools import wraps

def session_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'name' not in request.session:
            return redirect('user_sign_in')
        return view_func(request, *args, **kwargs)

    return wrapper

