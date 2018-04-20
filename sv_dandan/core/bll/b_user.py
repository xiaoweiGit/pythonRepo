import os, sys, uuid
from core.bll import bll, enum, decorator
from core.model.m_user import User

sys.path.append("os.path.abspath('.')\model")
from core.model.m_user import User


# @decorator.Auth(check=['user_id', 'phone'])
def addUser(user):
    """
    @ register a user
    @TODO:
    :param user:
    :return:
    """
    #     search
    u = bll.redis.r.hget(user.__name__, user.user_id)
    if u is None:
        user.user_id = uuid.uuid1()  # add uuid
        bll.redis.r.hset(user.__class__.__name__, user.user_id, user.__dict__)
        bll.logger.DEBUG(f"redis Hset set Name:{user.__class__.__name__},key:{user.user_id},value:{user.__dict__} ")
    else:
        return enum.APIErrorCode.AlreadyExist, enum.APIErrorCodeDescription.AlreadyExist

    return enum.APIErrorCode.Success, enum.APIErrorCodeDescription.Success


def delUser(id):
    """
    @ del User
    :param id:
    :return:
    """
    pass


def updateUser(user):
    """
    update
    :param user:
    :return:
    """
    pass


def getUser(user,isProcess=True,msg=""):
    """
    get
    :param msg:
    :param msg:
    :param user:
    :return:
    """
    if isProcess:
        u= bll.redis.r.hget(user.__class__.__name__,user.user_id)
        print(user.__class__,__name__)
        bll.logger.info("hello")
        if u is None:
            return [],enum.APIErrorCode.InvalidUid,enum.APIErrorCodeDescription.InvalidUid
        return eval(u),enum.APIErrorCode.Success,enum.API
    else:
        return [],enum.APIErrorCode.InvalidUid,enum.APIErrorCodeDescription.InvalidUid
