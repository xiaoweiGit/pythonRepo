from flask import jsonify,request

def Auth(**kw):
    """

    :param cls:
    :return:
    """

    def decorater(func):
        def checkAuth():
            pass

        def checkValidity(*args, **kwargs):
            print("------- %s" % args)
            print("------ %s " % kw)
            for key in kw:
                print(f"key:{key},value:{kw[key]}")

            # return func(*args, **kwargs)
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
        except :
            return jsonify({'code': -31993, 'data': {}, 'msg': '头部token认证失败'})
    return wrapper