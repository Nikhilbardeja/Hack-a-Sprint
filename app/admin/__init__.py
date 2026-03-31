from flask import Blueprint, session, redirect, url_for, jsonify


admin = Blueprint("admin", __name__, url_prefix="/admin/")


# @admin.before_request
# def restrict_to_admin():
#     if not session.get('loggedIn') or session.get('role') != 'admin':
#         session.clear()
#         return jsonify({"status": "error", "message": "Login Required!"}), 401


from .routes import *