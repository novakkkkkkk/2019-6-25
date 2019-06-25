from selenium import webdriver
import time
from public import login_zb,logout
import unittest

class TestCount(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    def test_one(self):
        driver = webdriver.Chrome('F:\driver\chromedriver_win32\chromedriver.exe')
        driver.get('http://120.79.59.41/#/login')
        driver.maximize_window()
        time.sleep(2)
        login_zb.login(driver)
        self.assertEqual(driver.title,'金康高科1')
        logout.logout(driver)

    def tearDown(self):
        print("测试结束")


if __name__ == '__main__':
    unittest.main()