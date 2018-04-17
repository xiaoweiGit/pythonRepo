# _*_ coding:utf-8 _*_

from core.jsonModel import jsonModel
@jsonModel()
class Friend_show:
    def __init__(self):
        self.cover=""
        self.showList=[]
