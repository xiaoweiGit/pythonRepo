#coding:utf-8
# @ Time :2018 /4/4
# @ File : api/view.py 
from api import api 
from flask import jsonify
import sys,os
sys.path.append(f"{os.path.abspath('.')}\conf")
import config

__author__ = 'bill'
tasks = [
    {
        'id': 1,
        'done': False,
        'url':f'{config.apiUrl}/user/account'
    },
    {
        'id': 1,
        'done': False,
        'url':f'{config.apiUrl}'
    }
]



@api.route(f'{config.apiUrl}/',methods=['GET'])
def d_get_tasks():
    return jsonify(tasks)

@api.route('/test')
def index():
    logger.info(index)
    # time.sleep(100000)
    logger.info("index_end")
    response={
            'result':1
            }
    return jsonify(response);
