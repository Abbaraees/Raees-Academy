from functools import wraps
from flask import session, redirect, url_for, abort


def require_role(role):
    def inner_decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            current_role = session.get('role')
            if not current_role:
                return redirect(url_for('auth.login'))

            if role != current_role:
                abort(401)

            return f(*args, **kwargs)

        return wrapped

    return inner_decorator



