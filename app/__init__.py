from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS

mysql = MySQL()
cors = CORS()

def createApp():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "FDSBJSFSH"


    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'grievance'
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["SESSION_COOKIE_SECURE"] = False
    app.config["UPLOADS"] = "./app/static/uploads"

    mysql.init_app(app)
    cors.init_app(
    app,
    supports_credentials=True,
    resources={r"/*": {"origins": ["http://10.225.245.193:5173","http://localhost:5173"]}}
)



    from .admin import admin
    from .officer import officer
    from .citizen import citizen
    from .auth import auth

    app.register_blueprint(admin)
    app.register_blueprint(officer)
    app.register_blueprint(citizen)
    app.register_blueprint(auth)

    return app