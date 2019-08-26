#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from public import login
from public import logout
import unittest
import HTMLTestRunner
import time

driver = webdriver.Chrome('F:\driver\chromedriver_win32_0625\chromedriver.exe')
class yyptTestCase(unittest.TestCase):

    def setUp(self):
        print('测试开始')


    def test_login_unusual(self):
        login.open(driver,'金康高科','guest','123456')
        self.assertEqual(driver.find_element_by_xpath('/html/body/div[2]/p').text,'公司名、用户名或密码错误',msg='提示信息不对')

    def tearDown(self):
        print('测试结束')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(yyptTestCase('test_login_unusual'))
    filepath =r'D:\Python project\yunyingpingtai\test_report\1.html'
    fp = open(filepath,'wb')
    #file_prefix = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    #fp = open(r'D:\Python project\yunyingpingtai2\test_report'+file_prefix+'_result.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'运营平台测试报告',description='测试用例执行情况')
    runner.run(suite)
    fp.close()