from flask import Blueprint, session, redirect, url_for


officer = Blueprint("officer", __name__, url_prefix="/officer/", template_folder="templates")


@officer.before_request
def restrict_to_admin():
    if not session.get('loggedIn') or session.get('role') != 'officer':
        session.clear()
        return redirect(url_for("auth.login"))


from .routes import *
from .pages import *