import os, sys, uuid
from core.bll import bll, enum
from core.model.m_user import User

sys.path.append("os.path.abspath('.')\model")
from core.model.m_user import User


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
