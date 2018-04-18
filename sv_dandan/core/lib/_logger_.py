# -*- coding:utf-8 =*- 
# @ Time :2018 /3/20 
# @ File : logger.py 
#import configparser 
import logging

__author__ = 'bill'

class Logger:

    __logger__=None
    def __init__(self,path,clevel=logging.DEBUG,Flevel=logging.DEBUG):
        logger=logging.getLogger(path)
        logger.setLevel(logging.DEBUG)
        
        fmt=logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s',
                '%Y-%m-%d %H:%M:%S')

        sh=logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)

        fh=logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(logging.DEBUG)

        logger.addHandler(sh)
        logger.addHandler(fh)

    def debug(self,msg):
        print("hello")
        print(logger)
        logger.debug(msg)

    def info1(self,msg):
        logger.info(msg)

    def warn(self,msg):
        logger.warn(msg)

    def error(self,msg):
        logger.error(msg)

    def critical(self,msg):
        logger.critical(msg)


    def getLogger(logsconfig):
        """
        @path:[]
        """
        if logsconfig is None: 
            return Logger(Logging.DEBUG,Logging.DEBUG)
        logger=logging.getLogger(logsconfig['SAVEPATH'])
        fmt=logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s',
                '%Y-%m-%d %H:%M:%S')
        if logsconfig["ISSHOWSCREEN"] ==True:
            sh=logging.StreamHandler(logsconfig["SLEVEL"])
            sh.setFormatter(fmt)
            logger.addHandler(sh) 
        
        fh=logging.FileHandler(logsconfig["SAVEPATH"])
        fh.setFormatter(fmt)
        fh.setLevel(logsconfig["FLEVEL"])
        logger.addHandler(fh)
        return logger
