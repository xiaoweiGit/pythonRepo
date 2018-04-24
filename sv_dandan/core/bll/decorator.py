import traceback

from flask import jsonify, request
from core.lib import authCheck
from core.bll import enum, bll


def Auth_checkIsNull(*kw):
    """

    :param cls:
    :return:
    """

    def decorater(func):
        def checkValidity(*args, **kwargs):
            waitCheck = None
            result = False
            if args.__len__() > 0 and args[0].__dict__ is not None:
                waitCheck = args[0]
            if kw.__len__() > 0 and waitCheck is not None:
                for key in kw:
                    print("_____ %s " % key)
                    if key in waitCheck.__dict__:
                        # check is null
                        result = authCheck.checkStringIsNull(waitCheck.__dict__[key])
                        if result is True:
                            break
                        print("--------- %s" % waitCheck.__dict__[key])
            if result:
                return enum.APIErrorCode.AuthParasError, enum.APIErrorCodeDescription.AuthParasError
            else:
                return func(*args, **kwargs)

        return checkValidity

    return decorater


def login_required(func):
    def wrapper(*args, **kwargs):
        # from middleware import unpack_token
        token = request.headers.get('Authorization')
        if token is None:
            return jsonify({'code': -9006, 'data': {}, 'msg': '头部token不允许为空'})
        try:
            # g.session_id_rpc = unpack_token(token)
            # g.token = token
            return func(*args, **kwargs)
        except:
            return jsonify({'code': -31993, 'data': {}, 'msg': '头部token认证失败'})

    return wrapper


def try_except(errors: object = (Exception,),
               default_value: object = [enum.APIErrorCode.Unknown_Error, enum.APIErrorCodeDescription.Unknown_Error]) -> object:
    def decorator(func):
        def new_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors as e:
                bll.logger.error(traceback.format_exc())
                return default_value

        return new_func

    return decorator
