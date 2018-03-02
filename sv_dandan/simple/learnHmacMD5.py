# -*- coding: utf-8 -*-
import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


md5time= hmac_md5("31b23f221123244efd493b2316f0c9",'1a4a9ac83ef8890a1cc447ff1494433c')


message = 'Hello, world!'.encode('utf-8')
key = 'secret'.encode('utf-8')
h = hmac.new(message,key , digestmod='MD5')
