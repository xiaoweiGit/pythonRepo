# _*_ coding:utf-8 _*_
from core.lib.jsonModel import jsonModel
@jsonModel()
class User:

    __name__="User"

    def __init__(self):
        self.user_id = ""
        self.password = ""
        self.Gender = 0
        self.birthday=""
        self.phone=""
        self.name=""
        self.Cons=0
        self.gps_info=""
        self.activity_time=""
        self.sign=""
        self.vip=""
        self.being_liked_num=0
        self.info=[]
        self.tag=[]
        self.Interest=[]
        self.answer=[]
        self.media=[]
        self.friend_show=[]
