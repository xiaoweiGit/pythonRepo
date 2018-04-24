import redis
from core.bll.decorator import try_except
import json
from core.model.m_response import response
from core.bll.enum import APIErrorCode, APIErrorCodeDescription

__author__ = 'bill'


class CRedis:
    def __init__(self, host='127.0.0.1', port=6379):
        self.host = host
        self.port = port
        self.db = 0
        self.r = redis.Redis(host=self.host, port=self.port, db=self.db, decode_responses=True)

    # set key-value (string)
    def set(self, key, value):
        return self.r.set(key, value)

    # set key-value no exist
    def setnx(self, key, value):
        return self.r.setnx(key, value)

    # set key-value by time
    def setex(self, key, value, time):
        return self.r.setex(key, time, value)

    def hset(self, name, key, value):
        return self.r.hset(name, key, value)

    @try_except(default_value=json.dumps(response(APIErrorCode.DBConfigError.value, APIErrorCodeDescription.DBConfigError.value).__dict__))
    def hget(self, name, key):
        return self.r.hget(name, key)

    def hdel(self, name, key):
        return self.r.hdel(name, key)
