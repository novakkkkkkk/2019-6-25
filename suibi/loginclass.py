# coding:utf-8
from selenium import webdriver
import unittest
import time

class login_go(unittest.TestCase):
    u'''登录类封装'''
    def login(self,companyname,username,password):
        self.driver = webdriver.Chrome('F:\driver\chromedriver_win32\chromedriver.exe')
        self.driver.get("http://120.79.59.41/#/login")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[1]/div/div/div[1]/input").send_keys(companyname)
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[2]/div/div/div[1]/input").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/form/div[3]/div/div/div[1]/input").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/button/span").click()
        time.sleep(3)


