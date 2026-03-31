from flask import Blueprint


officer = Blueprint("officer", __name__)


from .routes import *