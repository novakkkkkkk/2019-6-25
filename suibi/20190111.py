# coding:utf-8
from suibi.loginclass import login_go
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        print("==测试开始==")

    def tearDown(self):
        print("==测试结束==")

    def test_one(self):
        login_go().login("金康高科华中区","admin","123456")
        print("登陆成功")

if  __name__ == "__main__":
    unittest.main()


