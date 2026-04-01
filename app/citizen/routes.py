from flask import jsonify, request, current_app, flash, redirect, url_for, session
import os

from app import mysql

from app.Utils import generate_random_string


from app.citizen import citizen

@citizen.route("/add-complaint", methods=["POST"])
def addComplaints():
    data = request.form.to_dict()
    file = request.files.get("image")

    fileName = None
    
    if file:
        _, original_ext = os.path.splitext(file.filename)

        fileName = f"{generate_random_string(5)}{original_ext}"
        filepath = os.path.join(current_app.config['UPLOADS'], fileName)

        file.save(filepath)

    cur = mysql.connection.cursor()

    cur.execute("INSERT INTO complaints (id, title, description, location, image, citizenId, latitude, longitude, category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                 (generate_random_string(10), data.get("title"), data.get("description"), data.get("location"), fileName,
                   session.get("id"), data.get("latitude"), data.get("longitude"), data.get("category")))
    mysql.connection.commit()

    cur.close()

    flash("Complaint Regiseterd Successfully")

    return redirect(url_for("citizen.home"))