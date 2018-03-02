# -*- coding: utf-8 -*-
import http.client
import time
import urllib.request
import hashlib
import hmac

def mdsmssend(username,pwd,requesttime, signData,data):
#k坑货，只是因为加了一句
# <?xml version="1.0" encoding="utf-8"?>
# 结果给我来了个400错误，坑，巨坑

    
  #定义发送报文
   SoapMessage ='''
   <s:Envelope
        xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
        <s:Header>
            <h:Auths
                xmlns:h="http://tempuri.org/"
                xmlns="http://tempuri.org/"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xmlns:xsd="http://www.w3.org/2001/XMLSchema">
                <UserName>%s</UserName>
                <Password>%s</Password>
                <IsApp>true</IsApp>
                <RequestTime>%s</RequestTime>
                <SignData>%s</SignData>
                </h:Auths>
            </s:Header>
        <s:Body
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xmlns:xsd="http://www.w3.org/2001/XMLSchema">
            <GetResult  xmlns="http://tempuri.org/">
            <jsonData>%s</jsonData> 
            </GetResult>
            </s:Body>
        </s:Envelope>
   '''

   SoapMessage=SoapMessage % (username,pwd,requesttime,signData,data) 
   print(SoapMessage)
   texturl="https://superbuy.mplife.com/Interface/SuperBuyWebService.asmx?op=GetResult"
   # texturl="http://localhost:5468/SuperBuyWebService.asmx?op=GetResult"
   #连接到服务器后的第一个调用。它发送由request字符串到到服务器
   soapmessageLen="%d" % len(SoapMessage);
   headers = {"Host":"superbuy.mplife.com",
           "Content-type": "text/xml;charset=UTF-8",
           "Content-length":soapmessageLen,
           "SOAPAction":"http://tempuri.org/GetResult"}
   req=urllib.request.Request(texturl,data=SoapMessage.encode('utf-8'),headers=headers)
   r=urllib.request.urlopen(req)  
   s=r.read()
   print(s.decode('utf-8'))


def gethaslibvalue(value):
   # 创建H5对象
   m=hashlib.md5()
   m.update(value.encode('utf-8'))
   return m.hexdigest()

def gethmacvalue(key,value):
   return hmac.new(bytes(key,'utf-8'),bytes(value,'utf-8')).hexdigest()
   
def getMhacMD5(key,value):
   print("key=%s,value=%s" % (key,value))
   return hmac.new(key.encode('utf-8'),value.encode('utf-8'),digestmod='MD5').hexdigest()

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

if __name__=='__main__':
    requesttime= "%s" %int(time.time()) 
    uname='test'
    pword='31b23f212343311123453b2316f0c9'


    data="{\"Method\":115,\"Data\":\"{\\\"paging\\\":{\\\"PageIndex\\\":1,\\\"PageSize\\\":10,\\\"RecCount\\\":0},\\\"OrderNo\\\":\\\"WAP531466478\\\",\\\"Mobile\\\":\\\"13916109894\\\"}\"}"
    data="{\"Method\":115,\"Data\":\"{\\\"Mobile\\\":\\\"15001876277\\\",\\\"OrderNo\\\":\\\"APP563373844\\\"}\"}";

    requesttime='1516949253909' 
    # 对时间进行加密
    md5time= hmac_md5('',requesttime)
    print("%s-->%s" % (requesttime,md5time)) 
#   对时间进行hamc认证
    signdata=getMhacMD5(pword,md5time)
    signData=hmac_md5(pword,md5time)
    print("signdate hamc->%s" % signdata) 

    print(data.encode('gbk'))
    mdsmssend(uname,pword, requesttime,signdata,data)
