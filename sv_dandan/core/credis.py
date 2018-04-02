import redis

__author__='bill'
class CRedis:
    def __init__(self,host='127.0.0.1',port=6379):
        self.host=host
        self.port=port
        self.db=0
        sefl.r=redis.Redis(host=self.host,port=self.port,db=self.db)
    # set key-value (string)
    def set(self,key,value):
        return self.r.set(key,value)
   # set key-value no exist 
    def setnx(self,key,value):
        return self.r.setnx(key,value)
    # set key-value by time
    def setex(self,key,value,time):
        return self.r.setex(key,time,value)


    
