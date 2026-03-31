from flask import jsonify, session, request, redirect, url_for, flash
import MySQLdb

from app import mysql

from app.Utils import generate_random_string

from app.auth import auth



@auth.route("/api/login", methods=["POST"])
def loginApi():
    data = request.form.to_dict()

    session["email"] = data.get("email")

    query = lambda table : f"SELECT id, password FROM {table} WHERE email = %s"
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
            session['id'] = result.get("id")
            flash("Logged in successfully", "successs")
            return redirect(url_for("citizen.home"))
    flash("Invalid Credentials", "error")
    return redirect(url_for("auth.login"))



@auth.route("/api/signup", methods=["POST"])
def signupApi():
    data = request.form.to_dict()

    cur = mysql.connection.cursor()

    cur.execute("INSERT INTO citizens (id, name, email, password) VALUES (%s, %s, %s, %s)",
                 (generate_random_string(10), data.get("name"), data.get("email"), data.get("password"),))
    mysql.connection.commit()
    cur.close()
    flash("Account created successfully! Now you can login.", "success")
    return redirect(url_for("auth.login"))




@auth.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully", "success")
    return redirect(url_for("auth.login"))