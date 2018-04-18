import unittest
from core.bll.bll import logger, redis, fromJsonToModel
from core.model.m_user import User


class TestRedis(unittest.TestCase):
    def setup(self):
        pass

    def test_Hash(self):
        key = 'hello'
        value = 'world'
        redis.set(key, value)
        print(redis.r.get(key))
        self.assertEqual(redis.r.get(key), value)

    def test_Hash2dict(self):
        value = """ {'user_id': 123, 'password': '', 'Gender': 0, 'birthday': '', 'phone': '12321312', 'name': '', 'Cons': 0, 'gps_info': '', 'activity_time': '', 'sign': '', 'vip': '', 'being_liked_num': 0, 'info': [], 'tag': [], 'Interest': [], 'answer': [], 'media': [], 'Friend_show': []}
"""
        redis.r.hset("dic_name", "1", value)
        a = (redis.r.hget("dic_name", "1"))
        # print(type(a))
        # print(a)
        # print(value)
        # print(type(value))
        self.assertEqual(a, value)

    def test_Hash3dict(self):
        value = {'user_id': '123', 'password': '', 'Gender': '0', 'birthday': '', 'phone': '12321312', 'name': '',
                 'Cons': '0', 'gps_info': '', 'activity_time': '', 'sign': '', 'vip': '', 'being_liked_num': '0',
                 'info': [], 'tag': [], 'Interest': [], 'answer': [], 'media': [], 'Friend_show': []}
        for akey in value:
            redis.r.hset("test", akey, value[akey])
        a = redis.r.hgetall("test")
        print(type(a))
        print(value)
        print(a)
        self.assertEqual(value["user_id"], (redis.r.hget("test", "user_id")))
        # self.assertDictEqual(value,a)

    def test_Hash4dict(self):
        """将数据存入hset"""
        value = {'user_id': 123, 'password': '', 'Gender': 0, 'birthday': '', 'phone': '12321312', 'name': '',
                 'Cons': 0, 'gps_info': '', 'activity_time': '', 'sign': '', 'vip': '', 'being_liked_num': 0,
                 'info': [], 'tag': [], 'Interest': [], 'answer': [], 'media': [], 'Friend_show': []}
        valuestr = str(value)
        redis.r.hset("test1", value["user_id"], valuestr)
        getstr = redis.r.hget("test1", value["user_id"])
        self.assertEqual(getstr, valuestr)
        import json
        getdict = eval(getstr)
        self.assertDictEqual(value, getdict)
        self.assertEqual(value['user_id'], getdict["user_id"])

    def test_Hash5dict(self):
        """
        from Model to Redis ，then get dict to Model
        :return:
        """
        from core.model.m_user import User
        u = User()
        u.user_id = 1111
        u.phone = "2222222"
        print(u.__class__.__name__)
        redis.r.hset(u.__class__.__name__, u.user_id, u.__dict__)
        a = redis.r.hget(u.__class__.__name__, u.user_id)
        print(type(a))
        getdict= eval(a)
        n=User()
        n.fromJson(getdict)

        self.assertEqual(u.user_id,n.user_id)
        self.assertEqual(u.phone,n.phone)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
