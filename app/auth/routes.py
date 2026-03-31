from flask import jsonify, session, request
import MySQLdb

from app import mysql

from app.auth import auth



@auth.route("/login", methods=["POST"])
def login():
    data = request.json

    session["email"] = data.get("email")

    query = lambda table : f"SELECT password FROM {table} WHERE email = %s"
    print(data)
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(query(data.get("role")), (data.get("email"),))
    result = cur.fetchone()
    cur.close()
    print(query(data.get("role")))

    if result:
        if data.get("password") == result.get("password"):
            session["role"] = data.get("role")
            session["loggedIn"] = True

            return jsonify({"status": "success", "message": "Logged In Successfully"}), 200
        
    return jsonify({"status": "failed", "message": "Invalid Credentials"}), 401



@auth.route("/signup", methods=["POST"])
def signup():
    data = request.json

    cur = mysql.connection.cursor()

    cur.execute("INSERT INTO citizens (name, email, password) VALUES (%s, %s, %s)", (data.get("name"), data.get("email"), data.get("password")))
    mysql.connection.commit()
    cur.close()

    return jsonify({"status": "success", "message": "Regiseterd Successfully"}), 201



@auth.route("/check-login", methods=["POST", "GET"])
def checkLogin():
    role = ""
    # role = request.json.get("role")
    print(session)
    return jsonify({"loggedin": session.get("role") == role if session.get("role") else False}), 200 if (session.get("role") == role and session.get("role"))else 401

@auth.route("/logout")
def logout():
    session.clear()

    return jsonify({"status": "success", "message":"LoggedOut Successfully"}), 200