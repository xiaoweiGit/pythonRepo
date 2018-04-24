# coding:utf-8
# @ Time :2018 /4/4
# @ File : api/user.py

from core.api import api
from flask import request, json, jsonify

from core.bll import bll, b_user, enum, decorator
# from core.logger import Logge
from core.conf import config
from core.model.m_response import response, responseData
# sys.path.append(f"{os.path.abspath('.')}\model")
# from m_user import User
from core.model.m_user import User

tasks = [
    {
        'id': 1,
        'done': 'done',
        'url': f'{config.apiUrl}/user/account'
    },
    {
        'id': 2,
        'done': 'done',
        'url': f'{config.apiUrl}/user'
    }
]


@api.route(f'{config.apiUrl}/user', methods=['GET'])
def d_get_tasks():
    return jsonify(tasks)


@api.route(f'{config.apiUrl}/user/account', methods=['POST'])
def d_register():
    if request.method == 'POST':
        u = bll.fromJsonToModel(User.__name__, request.get_json())
        if not u.password.strip():
            return json.dumps(response().__dict__, ensure_ascii=False)
        # TODO:database opreation
        print(u)
        result = b_user.addUser(u)
        print(result)
    return json.dumps(
        responseData(result[1].value,
                     result[2].value,
                     result[0]
                     ).__dict__, ensure_ascii=False)


@api.route(f'{config.apiUrl}/user/<string:uid>', methods=['GET'])
@decorator.try_except(default_value=json.dumps(
    responseData([], enum.APIErrorCode.Unknown_Error.value, enum.APIErrorCodeDescription.Unknown_Error.value).__dict__,ensure_ascii=False))
def d_getUserInfo(uid):
    u = User()
    u.user_id = uid
    result = b_user.getUser(u)
    print(result)

    return json.dumps(
        responseData(result[1].value, result[2].value, result[0]).__dict__, ensure_ascii=False)


@api.route(f'{config.apiUrl}/user/<string:uid>', methods=['PUT'])
def d_updateUserInfo(uid):
    u = User()
    u.user_id = uid
    result = b_user.updateUser(u)

    return json.dumps(
        response(result[0].value, result[1].value).__dict__, ensure_ascii=False)
