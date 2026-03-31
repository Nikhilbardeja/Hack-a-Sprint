from flask import jsonify


from app.admin import admin


@admin.route("/")
def home():
    return "Admin"