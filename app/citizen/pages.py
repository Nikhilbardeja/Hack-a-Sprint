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
    data['inProgress'] = len(["inProgress" for complaint in result if complaint.get("status") == "inProgress"])
    return render_template("dashboard.html", data=data)


@citizen.route("/submit-complaint")
def submitComplaint():
    return render_template("submit-complaint.html")


@citizen.route("/public-feed")
def publicFeed():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM complaints WHERE date  >= CURDATE() - INTERVAL 0 DAY" )
    result = cur.fetchall()
    data = {}
    data['complaints'] = result
    data['length'] = len(result)
    data['resolved'] = len(["resolved" for complaint in result if complaint.get("status") == "resolved"])
    data['pending'] = len(["pending" for complaint in result if complaint.get("status") == "pending"])
    data['inProgress'] = len(["inProgress" for complaint in result if complaint.get("status") == "inProgress"])
    return render_template("PublicFeed.html", data=data)