import unittest
from core.bll.bll import logger,redis,fromJsonToModel
from core.model.m_user import User

class TestRedis(unittest.TestCase):
    def setup(self):
        pass


    def test_Hash(self):
        key='hello'
        value='world'
        redis.set(key,value)
        print(redis.r.get(key))
        self.assertEqual(redis.r.get(key),value)

    def test_Hash2dict(self):
        value=""""
        {'user_id': 123, 'password': '', 'Gender': 0, 'birthday': '', 'phone': '12321312', 'name': '', 'Cons': 0, 'gps_info': '', 'activity_time': '', 'sign': '', 'vip': '', 'being_liked_num': 0, 'info': [], 'tag': [], 'Interest': [], 'answer': [], 'media': [], 'Friend_show': []}
        """
        redis.r.hset("dic_name","1",value)
        a=str(redis.r.hgetall("dic_name"))
        print(type(a))
        # print(a)
        print(type(value))
        import json
        # print(json.loads(a))
       # b= fromJsonToModel(User.__name__,  a)
        # print(b)
        self.assertEqual(a,value)




    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()