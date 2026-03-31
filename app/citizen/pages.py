from flask import render_template, session
import MySQLdb
from app import mysql

from app.citizen import citizen


@citizen.route("/")
def home():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM complaints WHERE citizenid = %s", (session.get("id"), ))
    result = cur.fetchall()
    data = {}
    data['complaints'] = result
    data['length'] = len(result)
    data['resolved'] = len(["resolved" for complaint in result if complaint.get("status") == "resolved"])
    data['pending'] = len(["pending" for complaint in result if complaint.get("status") == "pending"])
    return render_template("citizen-home.html", data=data)