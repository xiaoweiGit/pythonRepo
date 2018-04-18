from core.lib.logger import Logger
from core.lib.c_redis import CRedis
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


def fromJsonToModel(o, re):
    """
     get request json to model
    :param o: __name
    :param re: request flask
    :return: model
    """
    u = globals()[o]()
    u.fromJson(re.get_json());
    logger.info(u.__dict__)
    return u


redis = __getcRedis__()
logger = __getlogger__()
