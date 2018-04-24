import os, sys, uuid
from core.bll import bll, enum, decorator
from core.model.m_user import User
import json

sys.path.append("os.path.abspath('.')\model")
from core.model.m_user import User


# @decorator.ExpHandler(decorator.myhandler, ())
@decorator.Auth_checkIsNull("password")
def addUser(user):
    """
    @ register a user
    @TODO:
    :param user:
    :return:
    """
    #     search
    # u = bll.redis.r.hget(user.__name__, user.user_id)
    # if u is None:
    user.user_id = str(uuid.uuid1())  # add uuid
    bll.redis.r.hset(user.__class__.__name__, user.user_id, user.__dict__)
    bll.logger.info(f"redis Hset set Name:{user.__class__.__name__},value:{user.__dict__} ")
    # else:
    #     return enum.APIErrorCode.AlreadyExist, enum.APIErrorCodeDescription.AlreadyExist

    return f"\"user_id\":\"{user.user_id}\"", enum.APIErrorCode.Success, enum.APIErrorCodeDescription.Success


@decorator.Auth_checkIsNull("user_id")
def delUser(user):
    """
    @ del User
    :param id:
    :return:
    """
    bll.redis.hset(user.__name__, user.user_id)
    bll.logger.info(f"redis Hdel set Name:{user.__class__.__name__}")
    return f"user_id:{user.user_id}", enum.APIErrorCode.Success, enum.APIErrorCodeDescription.Success


@decorator.Auth_checkIsNull("user_id", "password", "acount")
def updateUser(user):
    """
    update
    :param user:
    :return:
    """
    # search
    u = bll.redis.hget(user.__name__, user.user_id)
    if u is None:
        return [], enum.APIErrorCode.InvalidUid, enum.APIErrorCodeDescription.InvalidUid
    else:
        bll.redis.hset(user.__class__.__name__, user.user_id, user.__dict__)
        bll.logger.info(f"redis Hset set Name:{user.__class__.__name__},value:{user.__dict__} ")

    return f"user_id:{user.user_id}", enum.APIErrorCode.Success, enum.APIErrorCodeDescription.Success


@decorator.Auth_checkIsNull("user_id")
def getUser(user):
    """
    get
    :param msg:
    :param msg:
    :param user:
    :return:
    """
    u = bll.redis.hget(user.__class__.__name__, user.user_id)
    print(user.__class__, __name__)
    bll.logger.info("hello")
    if u is None:
        return [], enum.APIErrorCode.InvalidUid, enum.APIErrorCodeDescription.InvalidUid
    return eval(u), enum.APIErrorCode.Success, enum.APIErrorCodeDescription.Success
