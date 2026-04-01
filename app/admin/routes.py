from flask import jsonify, request, session, redirect, url_for
import MySQLdb
from datetime import datetime

from app import mysql

from app.admin import admin





@admin.route("/api/add-officer", methods=["POST"])
def apiAddOfficer():
    data = request.form.to_dict()

    cur = mysql.connection.cursor()

    cur.execute("INSERT INTO officer (name, email, password) VALUES (%s, %s, %s)",
                 (data.get("name"), data.get("email"), data.get("password")))
    mysql.connection.commit()

    cur.close()
    return redirect(url_for("admin.home"))

@admin.route("/get-data")
def getData():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cur.execute("SELECT * FROM complaints WHERE date  >= CURDATE() - INTERVAL 30 DAY" )
    data = cur.fetchall()
    cur.close()

    categories = list({complaint.get("category") for complaint in data})
    countList = []
    timeList = []
    for category in categories:
        count = 0
        tempTimeList = []
        for complaint in data:
            if category == complaint.get("category"): 
                count+=1
                if complaint.get("resolveDate"):
                    d1 = datetime.strptime(str(complaint.get("date")), "%Y-%m-%d")
                    d2 = datetime.strptime(str(complaint.get("resolveDate")), "%Y-%m-%d")

                    tempTimeList.append((d2 - d1).days)
        timeList.append(sum(tempTimeList) / len(tempTimeList) if tempTimeList else 0)
        countList.append(count)

    result = {"categoryData":{"labels": categories, "values": countList}, "timeData":{"labels": categories, "values": timeList}}
    print(result)
    return jsonify(result)


@admin.route("/data")
def data():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cur.execute("SELECT * FROM complaints" )
    data = cur.fetchall()
    cur.close()

    return jsonify(data)

@admin.route("api/complaints/delete/<id>", methods=["DELETE"])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM COMPLAINTS WHERE id = %s", (id, ))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for("admin.home"))