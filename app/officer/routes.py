from flask import jsonify, request, redirect, url_for
import MySQLdb

from app import mysql

from app.Utils import generate_random_string

from app.officer import officer



@officer.route("/get-complaints")
def getComplaints():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # Logic: (Status is NOT Resolved) OR (Status IS Resolved AND Date is within last 5 days)
    query = """
    SELECT * FROM complaints 
    WHERE status != %s 
    OR (status = %s AND date >= DATE_SUB(CURRENT_DATE, INTERVAL 5 DAY))
"""

# Pass the parameters (Status, Status)
    cur.execute(query, ('RESOLVED', 'RESOLVED'))
    data = cur.fetchall()
    cur.close()

    return jsonify(data)


@officer.route("/update-status/<id>", methods=["POST"])
def updateStatus(id):
    status = request.form.to_dict().get("status")

    cur = mysql.connection.cursor()

    cur.execute("UPDATE complaints SET status = %s WHERE id = %s", (status, id))
    mysql.connection.commit()

    cur.close()

    return redirect(url_for("officer.dashboard"))


@officer.route("/heatmap-data")
def heatMapData():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM COMPLAINTS")
    result = cur.fetchall()
    cur.close
    print(result)
    return jsonify(result)