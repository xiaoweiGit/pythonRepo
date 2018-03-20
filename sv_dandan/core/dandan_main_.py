import os
import sys
from flask import Flask

sys.path.append(f"{os.path.abspath('.')}\conf")
sys.path.append(f"{os.path.abspath('.')}\log")
import config
import logger

__author__ = 'bill'

app=Flask(__name__)

@app.route('/')
def index():
    return "hello dandan";


if __name__=="__main__":
    logger3=logger.Logger.getLogger(config.configs["LOG"])
    logger3.info("info")
    logger3.debug("debug")
    type(logger3)
    print("11 %s" %logger3)
    # app.run(host='0.0.0.0')
