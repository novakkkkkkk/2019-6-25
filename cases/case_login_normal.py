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

    def test_login_normal(self):
        login.open(driver,'金康高科','guest','789996')
        self.assertEqual(driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/ul/li/a[1]').text,'您好，总部管理员v',msg='账号名称不对')
        logout.logout(driver)

    def tearDown(self):
        print('测试结束')



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(yyptTestCase('test_login_normal'))
    filepath =r'D:\Python project\yunyingpingtai2\test_report\1.html'
    #fp = open(filepath,'wb')
    file_prefix = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    fp = open(r'D:\Python project\yunyingpingtai2\test_report'+file_prefix+'_result.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'运营平台测试报告',description='测试用例执行情况')
    runner.run(suite)
    fp.close()