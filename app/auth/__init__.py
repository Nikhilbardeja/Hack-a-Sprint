from flask import Blueprint

auth = Blueprint("auth", __name__)

from .routes import *
from .pages import *