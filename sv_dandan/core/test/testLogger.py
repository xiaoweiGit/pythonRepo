import unittest
import os,sys,logging
sys.path.append(os.path.abspath('..'))
from logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        print('setup')


    def test_log_info(self):
        logger=Logger(logging.Info,logging.INFO)
        logger.info('info')

    def test_log_debug(self):
        logger=Logger(logging.DEBUG,logging.DEBUG)
        logger.debug("DEBUG")

    def test_logfromConfg(self): 
        sys.path.append(f'{os.path.abspath("..")}\conf')
        import config
        print(config.configs["LOG"])
         
        logger3=logger.Logger.getLogger(config.configs["LOG"])
        logger3.info("info")

    def tearDown(self):
        print("tearDown")

if __name__=="__main__":
    unittest.main()
