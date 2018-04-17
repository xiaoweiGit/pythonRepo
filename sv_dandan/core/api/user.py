# coding:utf-8
# @ Time :2018 /4/4
# @ File : api/user.py 
import os
import sys

from api import api
from flask import request, json

from core.bll import bll, b_user
# from core.logger import Logge
from core.conf import config

# sys.path.append(f"{os.path.abspath('.')}\model")
# from m_user import User
from core.model.m_user import User
from core.model.m_response import response

tasks = [
    {
        'id': 1,
        'done': False,
        'url': f'{config.apiUrl}/user/account'
    }
]


@api.route('/user/account', methods=['POST'])
def d_register():
    if request.method == 'POST':
        u = bll.fromJsonToModel(User.__name__, request)
        if not u.password.strip():
            return json.dumps(response().__dict__,ensure_ascii=False)
        # TODO:database opreation
        b_user.addUser(u)

    return json.dumps(response(1,"接口调用成功！".__dict__,ensure_ascii=Flase))
