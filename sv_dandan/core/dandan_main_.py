from flask import Flask, jsonify, request, Blueprint

__author__ = 'bill'

app = Flask(__name__)
# log
# logger = Logger.getlogger()

# blueprint
from api import api

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
