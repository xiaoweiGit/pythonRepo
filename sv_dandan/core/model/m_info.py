# _*_ coding:utf-8 _*_

from core.lib.jsonModel import jsonModel
@jsonModel()
class Info:
    def __init__(self):
        self.industry=""
        self.work=""
        self.comp=""
        self.city=""
        self.hauntedly=""
