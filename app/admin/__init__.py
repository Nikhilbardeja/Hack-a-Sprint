from flask import Blueprint, session, redirect, url_for, jsonify


admin = Blueprint("admin", __name__, url_prefix="/admin/", template_folder="templates")


@admin.before_request
def restrict_to_admin():
    if not session.get('loggedIn') or session.get('role') != 'admin':
        session.clear()
        return redirect(url_for("auth.login"))


from .routes import *
from .pages import *