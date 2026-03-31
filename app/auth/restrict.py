from flask import session, redirect, url_for
from functools import wraps

def login_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not session.get('loggedIn') or session.get('role') != role:
                session.clear()
                return redirect(url_for('auth.login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator
