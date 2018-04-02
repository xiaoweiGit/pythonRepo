import os
import sys
from flask import Flask,jsonify,request

sys.path.append(f"{os.path.abspath('.')}\conf")
# sys.path.append(f"{os.path.abspath('.')}\log")
import config
import logger
import time

__author__ = 'bill'

app=Flask(__name__)

logger = logger.Logger.getlogger()

tasks = [
    {
        'id': 1,
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False,
        'url':f'{config.apiUrl/}'
    }
]

@app.route(f'{config.apiUrl}/',methods=['GET'])
def d_get_tasks():
    return jsonify(tasks)



@app.route('/test')
def index():
    logger.info(index)
    # time.sleep(100000)
    logger.info("index_end")
    response={
            'result':1
            }
    return jsonify(response);

@app.route('/SignUp',methods=['POST'])
def d_register():
    if request.method == 'POST':
        phone=request.form.get('phone')
        pwd=request.form.get('PassWord')
        
    return jsonify(request.form)
     
@app.route('/login',methods=['GET'])
def d_login():
    return "d_login";

if __name__=="__main__":
    logger.info(config.apiUrl)
    app.run(host='0.0.0.0',debug=True,threaded=True)
