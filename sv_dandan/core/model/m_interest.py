# _*_ coding:utf-8 _*_
from  core.jsonModel import jsonModel
@jsonModel()
class Interest:
    def __init__(self):
        self.sports=[]
        self.music=[]
        self.food=[]
        self.movie=[]
        self.booksAndComic=[]
        self.footprint=[]
