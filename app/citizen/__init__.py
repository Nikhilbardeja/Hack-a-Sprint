from flask import Blueprint


citizen = Blueprint("citizen", __name__, template_folder="templates")


from .routes import *
from .pages import *