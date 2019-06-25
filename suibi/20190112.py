#coding=utf-8
from selenium import webdriver
from public import login_zb
import unittest
import time


class  test_yypt(unittest.TestCase):
      def setUp(self):
          self.driver = webdriver.Chrome('F:\driver\chromedriver_win32\chromedriver.exe')
          self.base_url = "http://120.79.59.41/#/login"
          time.sleep(3)


      def test_lizi(self):
          driver = self.driver
          driver.get(self.base_url)
          #调用登录函数
          login_zb.login(driver)












