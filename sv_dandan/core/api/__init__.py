#codeing:utf-8
from flask import Blueprint

api=Blueprint('api',__name__,)

from api import user
from api import view
