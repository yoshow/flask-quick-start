from flask import Blueprint

apis = Blueprint('applications', __name__)

from . import application
