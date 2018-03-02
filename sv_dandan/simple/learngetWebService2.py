#encoding:UTF-8

import urllib
import urllib.request 
import time
import hashlib

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
                <IsApp>false </IsApp>
                <RequestTime>%s</RequestTime>
                <SignData></SignData>
                </h:Auths>
            </s:Header>
        <s:Body
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xmlns:xsd="http://www.w3.org/2001/XMLSchema">
            <GetResult
                xmlns="http://tempuri.org/">
                 <jsonData>
        {"Method":115,"Data":{"OrderNo":"WAP531466478","OrderId":"5fcdc4ff-1660-4c55-927a-563e50d05544","Mobile":"13916109894","UserId":"00000000-0000-0000-0000-000000000000","IsMixId":false,"TypeLabel":-1}}
      </jsonData>
                </GetResult>
            </s:Body>
        </s:Envelope>
'''

url = 'https://superbuy.mplife.com/Interface/SuperBuyWebService.asmx?op=GetResult'
print( (int(time.time())))
SoapMessage=SoapMessage % ('Relx','hanxiaowei',int(time.time()))
print (len(SoapMessage))
headers = {"Host":"superbuy.mplife.com",
           "Content-type": "text/xml;charset=UTF-8",
           "Content-length":"%d" % len(SoapMessage),
           "SOAPAction":"http://tempuri.org/GetResult"}

req=urllib.request.Request(url,headers=headers,data=SoapMessage.encode('UTF-8'))
r=urllib.request.urlopen(req)
s=r.read()
print(s)
print("END")
