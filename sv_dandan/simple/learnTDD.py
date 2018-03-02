import unittest
import sys

from learnHmacMD5 import hmac_md5

class TestHmacMD5(unittest.TestCase):
    def test_commonhmac(self):
        string=hmac_md5('123','123')
        print(sys._getframe().f_code.co_name)

    def test_teset1(self):
        self.assert_(1,1)

    def test_invalid(self):
         pass

if __name__=='__main__':
    unittest.main()
