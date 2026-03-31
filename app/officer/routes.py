from flask import jsonify, request
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


@officer.route("/update-status/<id>/<status>", methods=["PUT"])
def updateStatus(id, status):
    data = request.json

    cur = mysql.connection.cursor()

    cur.execute("UPDATE complaints SET status = %s WHERE id = %s", (status, id))
    mysql.connection.commit()

    cur.close()

    return jsonify({"status": "success", "message":"Complaint Updated Successfully"}), 200