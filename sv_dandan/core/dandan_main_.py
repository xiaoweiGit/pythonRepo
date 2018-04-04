import os
import sys
from flask import Flask,jsonify,request,Blueprint

from conf.config import *
# sys.path.append(f"{os.path.abspath('.')}\conf")
sys.path.append(f"{os.path.abspath('.')}\log")
# import config
from logger import Logger
import time


__author__ = 'bill'

app=Flask(__name__)
# log
logger = Logger.getlogger()

# blueprint
from api import api
app.register_blueprint(api) 

if __name__=="__main__":
     logger.info(configs)
     logger.info(apiUrl)
     app.run(host='0.0.0.0',debug=True,threaded=True)
