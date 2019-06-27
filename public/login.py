# coding:utf-8
from selenium import webdriver
import time

def login(self,companyname,username,psw):
        self.driver=webdriver.Chrome("F:\driver\chromedriver_win32_0625\chromedriver.exe")
        url="http://120.79.59.41:81/#/login"
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def login(self,companyname,username,psw):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[2]/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[3]/form/div[1]/div/div/div/input').send_keys(companyname)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[3]/form/div[2]/div/div/div/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[3]/form/div[3]/div/div/div/input').send_keys(psw)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[3]/div/button/span').click()
        time.sleep(3)
