from flask import jsonify, request, session
import json

from app import mysql

from app.admin import admin


@admin.route("/")
def home():
    return "Admin"



@admin.route("/add-officer", methods=["POST"])
def addOfficer():
    data = request.json

    cur = mysql.connection.cursor()

    cur.execute("INSERT INTO officers (name, email, password, address) VALUES (%s, %s, %s, %s)",
                 (data.get("name"), data.get("email"), data.get("password"), data.get("address")))
    mysql.connection.commit()

    cur.close()
    return jsonify({"status": "success", "message": "Regiseterd Successfully"}), 201

@admin.route("/heatmap")
def heatMap():
    cur = mysql.connection.cursor()

