# coding:utf-8
# @ Time :2018 /4/4
# @ File : api/user.py

from api import api
from flask import request, json

from core.bll import bll, b_user,enum
# from core.logger import Logge
from core.conf import config
from core.model.m_response import response
# sys.path.append(f"{os.path.abspath('.')}\model")
# from m_user import User
from core.model.m_user import User

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
        result=b_user.addUser(u)
    return json.dumps(
        response(result[0].value,
                 result[1].value
                 ).__dict__,ensure_ascii=False)
