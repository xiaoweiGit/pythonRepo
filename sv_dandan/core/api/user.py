# coding:utf-8
# @ Time :2018 /4/4
# @ File : api/user.py 
from api import api 
from flask import jsonify, request, json
import sys, os
from core.logger import Logger

logger = Logger.getlogger()

sys.path.append(f"{os.path.abspath('.')}\model")
from m_user import User 
tasks=[
        {
        }    
    ]


@api.route('/SignUp',methods=['POST'])
def d_register():
    if request.method == 'POST':
        phone=request.form.get('phone')
        pwd=request.form.get('PassWord')
        logger.info(request.data)
        # u=User().fromJson(json.loads(request.data))
        # print(request.data)

        # print(u.__dict__)
    return json.dumps(request.get_json())

@api.route('/txx')
def txx():
    pass 
