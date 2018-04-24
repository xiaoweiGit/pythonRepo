import unittest
from core.bll.enum import APIErrorCode,APIErrorCodeDescription
from core.api import user
import http.client
import json
from core.model.m_user import User
from core.model.m_response import response,responseData
from core.bll import bll



class TestUser(unittest.TestCase):
    path = "127.0.0.1"
    port = 5000
    url = "/dandan/api/v0.1/user"
    data = """
        {"Cons": 10, "Gender": 1, "Interest": [], "activity_time": "yyyy-MM-dd HH:mm:ss", "answer": [{"a": "你怎么这么帅?", "q": "天生的"}, {"a": "你怎么这么帅?", "q": "我不介意再回答你一次"}], "being_liked_num": 999, "birthday": "1992-10-08", "friend_show": {"cover": "http://asdfa", "showList": [{"media": [{"order": 2, "type": 1, "url": "http://asf"}, {"order": 2, "type": 1, "url": "http://asf"}, {"order": 2, "type": 1, "url": "http://asf"}], "time": "yyyy-MM-dd HH:mm:ss", "title": "又被帅醒"}]}, "gps_info": "11.12345678,11,12345678", "info": {"city": "上海", "comp": "文思海辉", "hauntedly": "", "industry": "it", "work": "android"}, "media": [{"order": 2, "type": 1, "url": "http://asf"}, {"order": 1, "type": 1, "url": "http://asf"}, {"order": 3, "type": 1, "url": "http://asf"}], "name": "Lee", "password": " 123", "phone": "13122279802", "sign": "", "tag": ["帅", "酷"], "user_id": "71c2a4a6-46d1-11e8-ae93-005056c00008", "vip": "0"}
        """

    def setup(self):
        pass

    def test_UserAdd_1(self):
        str = json.loads(self.data)
        print(str)
        headers = {"Content-Type": "application/json","Host":"127.0.0.1:5000"}
        conn = http.client.HTTPConnection(self.path, port=self.port)
        conn.request("POST",f"{self.url}/account", self.data.encode('utf-8'), headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        rd= bll.fromJsonToModel(responseData.__name__,json.loads(data))
        self.assertEqual(rd.code,APIErrorCode.Success.value)
        print(rd.data)
        u=eval(rd.data)
        self.assertIsNotNone(u)
        self.userid=u.user_id





    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
