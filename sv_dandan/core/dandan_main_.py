import sys,os
from flask import Flask, jsonify, request, Blueprint

sys.path.append(os.path.abspath(".."))
__author__ = 'bill'

app = Flask(__name__)
# log
# logger = Logger.getlogger()

# blueprint
from core.api import api

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
