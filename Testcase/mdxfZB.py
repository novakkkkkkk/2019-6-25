#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver
from public import login
from public import logout
import time

file = r'C:\Users\andreprevin\Desktop\新运营平台\测试用图片\5.jpg'
driver = webdriver.Chrome('F:\driver\chromedriver_win32_0625\chromedriver.exe')
login.open(driver,'金康高科','guest','789996')
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/ul/li[2]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="menu_left"]/ul/li[4]/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[6]/div/div/input').send_keys('刘哲小店')
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[2]/div[1]/form/button[1]/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[14]/div/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/span').click()
time.sleep(2)
driver.find_element_by_name('fileX').send_keys(file)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[2]/div/div[1]/div[6]/div/div[3]/div/button[1]/span').click()
time.sleep(2)
logout.logout(driver)
