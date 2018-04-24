from core.lib.logger import Logger
from core.lib.c_redis import CRedis
from core.bll import decorator
from core.model.m_response import response
from core.bll.enum import APIErrorCodeDescription, APIErrorCode
import json
from core.model import *
import logging

_redis = None


def __getcRedis__() -> object:
    global _redis
    if _redis is None:
        from core.conf import config
        _redis = CRedis(config.configs["DB"]["IP"], config.configs["DB"]["PORT"])
    return _redis


_logger: None = None


def __getlogger__() -> object:
    global _logger
    if _logger is None:
        _logger = Logger()
        _logger.setup_logging()
    return logging


def fromJsonToModel(o, jn):
    """
     get request json to model
    :param o: __name
    :param re: request flask
    :return: model
    """
    u = globals()[o]()
    u.fromJson(jn);
    logger.info(u.__dict__)
    return u


logger = __getlogger__()
redis = __getcRedis__()
