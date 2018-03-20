# -*- coding:utf-8 =*- 
# @ Time :2018 /3/20 
# @ File : logger.py 
#import configparser 
import logging

__author__ = 'bill'

class Logger:
    def __init__(self,path,clevel=logging.DEBUG,Flevel=logging.DEBUG):
        self.logger=logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        
        fmt=logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s',
                '%Y-%m-%d %H:%M:%S')

        sh=logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)

        fh=logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(logging.DEBUG)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self,msg):
        self.logger.debug(msg)

    def info1(self,msg):
        self.logger.info(msg)

    def warn(self,msg):
        self.logger.warn(msg)

    def error(self,msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)


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
            print(logsconfig)
        
        fh=logging.FileHandler(logsconfig["SAVEPATH"])
        fh.setFormatter(fmt)
        fh.setLevel(logsconfig["FLEVEL"])
        logger.addHandler(fh)
        return logger
