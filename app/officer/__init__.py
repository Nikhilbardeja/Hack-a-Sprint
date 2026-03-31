from flask import Blueprint


officer = Blueprint("officer", __name__, url_prefix="/officer/")


from .routes import *