# codeing:utf-8
from flask import Blueprint

api = Blueprint('api', __name__, )

from core.api import user
from core.api import view
