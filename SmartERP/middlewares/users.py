from django.db.models import Model

try:
    from threading import local, current_thread
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()


class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        setattr(_thread_locals, f'user_{current_thread().name}', request.user)
        # setattr(_thread_locals, 'device_{0}'.format(current_thread().name), get_device_type(request))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        key = f'user_{current_thread().name}'

        if hasattr(_thread_locals, key):
            delattr(_thread_locals, key)

        return response


def get_signed_in_user():
    return get_current_user() if isinstance(get_current_user(), Model) else None


def get_current_user():
    return getattr(_thread_locals, 'user_{0}'.format(current_thread().name), None)


def get_current_user_id():
    user = get_current_user()
    return user.id if user else None
