# -*- coding:utf-8 =*- 
# @ Time :2018 /3/20 
# @ File : config_default.py 
# import configparser 
import os,sys
import logging
__author__ = 'bill'

configs={
        'DB':{
                'IP':'127.0.0.1',
                'PORT':6379,
                'USER':'bill',
                'PWD':'1qaz2wsx',
                'DB':'dandan'
            },
        'DBTYPE': 'Redis',
        'LOG':{
                'ISSHOWSCREEN':True,# is print cmd
                'SAVEPATH':f'{os.path.abspath("..")}\logs\log.txt',
                'SLEVEL':logging.DEBUG,# print cmd  level
                'FLEVEL':logging.DEBUG, #print file leve 
            },
        'SETTING':{
                'RESPONSETYPE':'json',# supoort  onlyjson 
                'VERSION':'v0.1',
                'APINAME':'dandan',
                }
        }


