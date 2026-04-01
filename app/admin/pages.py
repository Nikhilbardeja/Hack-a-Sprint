from flask import render_template, redirect, url_for


from app import mysql

from app.admin import admin


@admin.route("/")
def home():
    return render_template("dashboard.html")


@admin.route("/add-officer")
def addOfficer():
    return render_template("add-officer.html")

@admin.route("/overdue")
def overdue():
    return render_template("overdue.html")