from flask import Blueprint


citizen = Blueprint("citizen", __name__)


from .routes import *