from flask import Flask


def createApp():
    app = Flask(__name__)



    from .admin import admin
    from .officer import officer
    from .citizen import citizen

    app.register_blueprint(admin)
    app.register_blueprint(officer)
    app.register_blueprint(citizen)

    return app