from flask import render_template
import MySQLdb

from app import mysql

from app.officer import officer


@officer.route("/")
def home():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM complaints")
    data = {}
    data['complaints'] = cur.fetchall()
    cur.close()
    return render_template("officer-dashboard.html", data=data)


@officer.route("/heatmap")
def heatmap():
    return render_template("officer-heatmap.html")